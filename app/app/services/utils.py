import json
import os
import typing as t
from difflib import SequenceMatcher

from app import config


def read_departments_json() -> t.List[t.Dict[str, t.Any]]:
    """Parse 'departments.json' as dict."""
    with open(os.path.join(config.PROJECT_DIR, config.DEPARTMENTS_JSON_FILENAME)) as f:
        return json.load(f).get('departments')


def calculate_string_similarity(str_1: str, str_2: str) -> int:
    """Calculate similarity ratio of given strings as a rounded percentage."""
    s = SequenceMatcher(None, str_1, str_2)
    return int(round(s.ratio(), 2) * 100)
