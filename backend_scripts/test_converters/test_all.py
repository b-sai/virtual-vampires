import unittest
import test_english


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_english.TestEnglish))
    # add other test modules here
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
