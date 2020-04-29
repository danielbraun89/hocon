from typing import Any, TextIO, AnyStr, Dict
from pyhocon import ConfigFactory, HOCONConverter
import json

__version__ = "0.0.2"


def dump(obj: Any, fp: TextIO, **kwargs):
    json.dump(dumps(obj), fp, **kwargs)


def dumps(obj: Any, **kwargs) -> str:
    return HOCONConverter.to_json(obj, **kwargs)


def load(fp: TextIO) -> Dict[str, Any]:
    return loads(fp.read())


def loads(s: AnyStr) -> Dict[str, Any]:
    hocon_obj = ConfigFactory.parse_string(s)
    return json.loads(HOCONConverter.to_json(hocon_obj))
