from typing import Any, TextIO, AnyStr, Dict
from pyhocon import ConfigFactory, HOCONConverter
import json

__version__ = "0.0.1"


def dump(obj: Any, fp: TextIO):
    json.dump(dumps(obj), fp)


def dumps(obj: Any) -> str:
    return HOCONConverter.to_json(obj)


def load(fp: TextIO) -> Dict[str, Any]:
    return loads(fp.read())


def loads(s: AnyStr) -> Dict[str, Any]:
    hocon_obj = ConfigFactory.parse_string(s)
    return json.loads(HOCONConverter.to_json(hocon_obj))
