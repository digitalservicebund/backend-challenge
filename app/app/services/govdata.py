import typing as t

import requests

GOV_DATA_CKAN_API_BASE = 'https://www.govdata.de/ckan/api/3/action'
API_ENDPOINT_ORGANIZATION_LIST = '/organization_list'


def get_department_metadata() -> t.List[t.Dict[str, t.Any]]:
    """Query GovData API for list of organisations and their metadata."""
    query_params = {
        'all_fields': True,
        'include_dataset_count': True,
        'limit': 100,
    }
    response = requests.get(
        url=GOV_DATA_CKAN_API_BASE + API_ENDPOINT_ORGANIZATION_LIST,
        params=query_params,
    )
    if not response.status_code == 200:
        raise Exception(f'Failed to load data from DataGOV API w/ status code {response.status_code}')
    data = response.json()
    if not data['success']:
        raise Exception('Failed to load data from DataGOV API w/ error %s' % data['error']['message'])
    return data['result']
