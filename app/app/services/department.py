import typing as t

from app.services.utils import calculate_string_similarity


def _parse_department_names(departments: t.List[t.Dict[str, str]]) -> t.Generator[str, t.Any, None]:
    """Generate names of ministries and subordinates thereof."""
    for item in departments:
        if 'name' in item:
            yield item['name']
        if 'subordinates' in item:
            yield from _parse_department_names(item['subordinates'])


def _flatten_department_names(departments: t.List[t.Dict[str, str]]) -> t.List[str]:
    """Flatten names in departments.json."""
    return [name for name in _parse_department_names(departments)]


def _is_ministry_or_subordinate_thereof(title: str, department_names: t.List[str]) -> bool:
    keywords = ['bundesministerium', 'bundesanstalt', 'bundesamt']
    return title in department_names or any([kw in title.lower() for kw in keywords])


def _get_department_package_count(
        json_name: str,
        names_in_json_not_in_api: t.List[str],
        names_in_api_not_in_json: t.List[str],
        department_package_count_map: t.Dict[str, int],
) -> int:
    """If department name from JSON is in names_in_json_not_in_api
        find match using similarity > 80% in names_in_api_not_in_json
        take package_count from metadata using API department name first,
        otherwise name from json, returning 0 is no entry for either name is found."""
    api_name = None
    if json_name in names_in_json_not_in_api:
        matches = [n for n in names_in_api_not_in_json if calculate_string_similarity(json_name, n) >= 80]
        api_name = matches[0] if len(matches) else None
    dep_name = api_name if api_name else json_name
    return department_package_count_map.get(dep_name, 0)


def _package_count_generator(item,
                             names_in_json_not_in_api: t.List[str],
                             names_in_api_not_in_json: t.List[str],
                             department_package_count_map: t.Dict[str, int]) -> t.Generator[int, t.Any, None]:
    """Generate package counts for ministries and their subordinates."""
    dep_name = item['name']
    if 'subordinates' in item:
        for subordinate in item['subordinates']:
            yield from _package_count_generator(subordinate,
                                                names_in_json_not_in_api,
                                                names_in_api_not_in_json,
                                                department_package_count_map)
    yield _get_department_package_count(dep_name,
                                        names_in_json_not_in_api,
                                        names_in_api_not_in_json,
                                        department_package_count_map)


def aggregate_dataset_counts_by_ministry(
        all_department_metadata: t.List[t.Dict[str, t.Any]],
        departments_with_subordinates: t.List[t.Dict[str, t.Any]],
) -> t.List[t.Dict[str, t.Any]]:
    """Aggregate dataset counts for each ministry and all its subordinates.

    There are discrepancies between department names in departments.json and names from the api.
    In order to aggregate data for each ministry and all it subordinates we have use the structure
    from departments.json and counts from the api metadata.
    This function uses the utility "_get_department_package_count" to get the count (see docstring).
    """
    # create a flat list of ministry and subordinated agencies' names
    department_names = _flatten_department_names(departments_with_subordinates)
    # create a map of department name (API) to number of packages
    department_package_count_map = {dep['title']: dep['package_count']
                                    for dep in all_department_metadata
                                    if _is_ministry_or_subordinate_thereof(dep['title'], department_names)}

    api_set = set(department_package_count_map.keys())
    json_set = set(department_names)
    names_in_api_not_in_json = api_set - json_set
    names_in_json_not_in_api = json_set - api_set

    for dep in departments_with_subordinates:
        dep['package_count'] = sum(_package_count_generator(dep,
                                                            list(names_in_json_not_in_api),
                                                            list(names_in_api_not_in_json),
                                                            department_package_count_map))

    return sorted(departments_with_subordinates, key=lambda d: d['package_count'], reverse=True)
