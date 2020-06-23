import json
from typing import Any, TextIO

from pyhocon import HOCONConverter


def dump(obj: Any, fp: TextIO, **kwargs):
    json.dump(dumps(obj), fp, **kwargs)


def dumps(obj: Any, **kwargs) -> str:
    return HOCONConverter.to_json(obj, **kwargs)
