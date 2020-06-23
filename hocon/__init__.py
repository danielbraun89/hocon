from typing import Any, TextIO, AnyStr, Dict
from pyhocon import ConfigFactory, HOCONConverter
import json
from hocon import encoder

__version__ = "0.1.0"

dump = encoder.dump
dumps = encoder.dumps


def load(fp: TextIO) -> Dict[str, Any]:
    return loads(fp.read())


def loads(s: AnyStr) -> Dict[str, Any]:
    hocon_obj = ConfigFactory.parse_string(s)
    return json.loads(HOCONConverter.to_json(hocon_obj))
