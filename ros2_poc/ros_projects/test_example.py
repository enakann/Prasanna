import unittest
import sys

def func(i):
    return 1/i


class MyTest(unittest.TestCase):

    def _helper(self,a):
        try:
            return func(a)
        except Exception:
            sys.exit()


    def test1(self):
        ret=self._helper(0)
        self.assertEqual(2,ret)

    def test2(self):
        ret=self._helper(1)
        self.assertEqual(1,ret)




if __name__ == '__main__':
    unittest.run(failfast=True)

