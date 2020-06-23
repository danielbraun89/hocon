import json
from typing import Any, TextIO, AnyStr, Dict

from pyhocon import ConfigFactory, HOCONConverter


def load(fp: TextIO) -> Dict[str, Any]:
    return loads(fp.read())


def loads(s: AnyStr) -> Dict[str, Any]:
    hocon_obj = ConfigFactory.parse_string(s)
    return json.loads(HOCONConverter.to_json(hocon_obj))
