import unittest

if __name__ == '__main__':
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=3).run(tests)
