import json
import os
from typing import Any, TextIO, AnyStr, Dict

from pyhocon import ConfigFactory, HOCONConverter


def load(fp: TextIO) -> Dict[str, Any]:
    return loads(fp.read(), basedir=os.path.dirname(fp.name))


def loads(s: AnyStr, **kwargs: Any) -> Dict[str, Any]:
    hocon_obj = ConfigFactory.parse_string(s, **kwargs)
    return json.loads(HOCONConverter.to_json(hocon_obj))
