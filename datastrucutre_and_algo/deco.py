import time


def deco(func):
    def inner(*args,**kwargs):
        print(func)
        t1=time.time()
        ret=func(*args,**kwargs)     #
        t2=time.time()
        print(f"total time taken is {t2-t1}")
        return ret
    return inner


@deco
def func1(a,b):
    time.sleep(2)
    return a+b


@deco
def func2(a,b):
    return a-b

@deco
class A:
    def method1(self):


print(func1(5,1))
print(func2(5,2))

