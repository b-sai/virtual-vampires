import unittest
from . import test_english
import os

def suite():
    print("TESTING IN SUITE ------------")
    print(os.environ["DEMO"], "--**")

    test_loader = unittest.TestLoader()
    test_names = ['_backend.backend_scripts.test_converters.test_english',
                  '_backend.backend_scripts.test_converters.test_swahili',
                  '_backend.backend_scripts.test_converters.test_spanish']

    test_suite = test_loader.loadTestsFromNames(test_names)

    # add other test modules here
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())