from unittest import TestCase
import os
import hocon
from io import StringIO


class TestHocon(TestCase):
    test_file_path = os.path.join(os.path.dirname(__file__), "resources", "hocon_test_file.conf")

    # This example is from https://github.com/chimpler/pyhocon/blob/master/README.md
    example_hocon = \
        """ 
        {
          databases {
            # MySQL
            active = true
            enable_logging = false
            resolver = null
            # you can use substitution with unquoted strings. If it it not found in the document, it defaults to environment variables
            home_dir = ${HOME} # you can substitute with environment variables
            "mysql" = {
              host = "abc.com" # change it
              port = 3306 # default
              username: scott // can use : or =
              password = tiger, // can optionally use a comma
              // number of retries
              retries = 3
            }
          }
          // this will be appended to the databases dictionary above
          databases.ips = [
            192.168.0.1 // use white space or comma as separator
            "192.168.0.2" // optional quotes
            192.168.0.3, # can have a trailing , which is ok
          ]
        }
        """

    def test_loads(self):
        a = hocon.loads(self.example_hocon)
        self.assertIsInstance(a, dict)

    def test_load(self):
        str_io = StringIO(self.example_hocon)
        hocon_obj = hocon.load(str_io)
        self.assertIsInstance(hocon_obj, dict)

    def test_dumps(self):
        hocon_obj = hocon.loads(self.example_hocon)
        str_hocon = hocon.dumps(hocon_obj)
        self.assertIsInstance(str_hocon, str)
