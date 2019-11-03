import threading
import time


class Singleton:
    _instance=None
    def __new__(cls,*args,**kwargs):
        print(cls)
        print(args)
        print(kwargs)
        if  cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance

class SingletonMeta(type):
    _instance=None
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance=super().__call__(*args,**kwargs)
        return self._instance

class Client:
    _instance=None
    _init=None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance=super(Client,cls).__new__(cls)
        return cls._instance

    def __init__(self,a):
        if self._init:
            return
        self._init=True
        self.a=a
        self.running=True
        self.t1=threading.Thread(target=self.work,args=(),daemon=False)
        self.t1.start()


    def work(self):
        while self.running:
            time.sleep(1)
            print(self.a)
            self.a+=1

    def stop(self):
        self.running=False
        self.t1.join()

    def __del__(self):
        self.state=False
        self.t1.join()



if __name__ == '__main__':
    c1=Client(10)
    c2=Client(11)
    print(id(c1)==id(c2))
    time.sleep(3)
    c2.stop()
