from hocon import decoder
from hocon import encoder

__version__ = "0.1.0"

dump = encoder.dump
dumps = encoder.dumps

load = decoder.load
loads = decoder.loads
