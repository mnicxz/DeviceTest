import unittest
from case import Test_01

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    run = unittest.TextTestRunner(verbosity=2)

    suite.addTest(loader.loadTestsFromModule(Test_01))
    run.run(suite)