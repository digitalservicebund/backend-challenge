import json
import os
import typing as t

from app import config


def read_departments_json() -> t.List[t.Dict[str, t.Any]]:
    """Parse 'departments.json' as dict."""
    with open(os.path.join(config.PARENT_DIR, config.DEPARTMENTS_JSON_FILENAME)) as f:
        return json.load(f).get('departments')
