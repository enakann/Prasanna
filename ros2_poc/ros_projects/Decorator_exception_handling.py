import unittest
import os
import sys
from functools import update_wrapper, partial

#import pdb;pdb.set_trace()

class B:
    def stop(self):
        print("stop exexuton")

class ExceptionHandler:
    def __init__(self,func):
        print("3.Deco init")
        update_wrapper(self,func)
        self.func=func
        self._exitm=os._exit
        self.cleanup=B().stop

    def __get__(self, obj, objtype):
        """Support instance methods."""
        print("4.get is called")
        return partial(self.__call__, obj)

    def __call__(self, obj, *args, **kwargs):
        try:
            print("5.__call__ is called")
            print(self.func.__doc__)
            return "Result inide decaorator is {}".format(self.func(obj, *args, **kwargs))
        except ZeroDivisionError:
            self.cleanup()
            self._exitm(255)



class A:
    def __init__(self,a):
        print("1.init called")
        self.a=a

    @ExceptionHandler
    def execute(self,b):
        """ this is a doc string"""
        print(self.execute)
        print("2.in execute method")
        return self.a/b

    def stop(self):
        print("stop program")




#obj=A(10)
#obj.execute(2)
#obj.execute(0)


class Helper:

    def __init__(self,a):
        self.a=a

    def execute(self,b):
        raise RuntimeError
        return self.a/b

    def stop(self):
        print("clean up")


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.helper=Helper(1)

    @ExceptionHandler
    def _helper(self,i):
        try:
            try:
                return self.helper.execute(i)
            finally:
                self.helper.stop()
        except ZeroDivisionError:
            os._exit(251)
            #sys.exit()


    def test1(self):
        ret=self._helper(0)
        self.assertEqual(ret,4)


    def test2(self):
        ret=self._helper(0)
        self.assertEqual(ret,5)



if __name__ == '__main__':
    unittest.main(failfast=True)



