import unittest
from . import test_english


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_english.TestEnglish1()))

    # add other test modules here
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest=suite())
