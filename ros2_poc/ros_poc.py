import threading
from threadwrapper import ThreadWrapper
from time import sleep
from singleton import Singleton
import random
import os
import asyncio

class Consumer:
    def __init__(self):
        #self.callback=os.environ['OVERRIDE']()
        self.callback=None
        #self.thread1=ThreadWrapper(self,'daemonMode')
        #self.thread1.daemon=True
        #self.thread1.start()
        #self.daemonMode()

    def set_callback(self,obj,method):
        self.callback=getattr(obj,method)

    def spin(self):
        return self.callback()


class Base(metaclass=Singleton):
    Topic=None
    def __init__(self):
        self.a=0
        self._frontbutton=None
        self.thread2=ThreadWrapper(self,'publish')
        self.thread2.daemon=True
        self.thread2.start()


    def callback(self,a):
        #import pdb;pdb.set_trace()
        self.frontbutton = a

    def publish(self):
        sleep(1)
        print(f"{self.TOPIC} -- > {self.MSG}")

    @property
    def frontbutton(self):
        return self._frontbutton

    @frontbutton.setter
    def frontbutton(self, val):
        self._frontbutton = val
        if val:
            self.frontbuttonInteration(val)

    def stop_publishing(self):
        self.thread2.stop()

    def getcallback(self):
        return os.environ['OVERRIDE']()



class ACC(Base):
    TOPIC='ACC'
    MSG=0

    def break_override(self):
        self.MSG+=1

    def frontbuttonInteration(self,val):
        self.break_override(val)

class LCC(Base):
    TOPIC='LCC'
    MSG=999

    def break_override(self):
        self.MSG+=1

    def frontbuttonInteration(self,val):
        self.break_override(val)




class Client:
    _singleton = None

    def __init__(self):

        self.map={
            'ACC':ACC,
            'LCC':LCC
        }
        self.consumer = Consumer()
        self.override_obj=self.map.get(os.getenv('OVERRIDE'))()
        self.set_callback()

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Client, cls).__new__(cls,*args,**kwargs)
        return cls._singleton

    def get_obj(self,name):
        return self.map[name]
        #self.obj=self.map.get(os.getenv('OVERRIDE'))()
        #self.thread2=ThreadWrapper(self,'startc')
        #self.thread2.start()
    def set_callback(self):
        self.consumer.set_callback(self.override_obj,'publish')

    async def run(self):
        self.set_callback()
        await self.consumer.spin()
    def get_overrideobj(self):
        return self.override_obj

    def stop_publishing(self):
        self.override_obj.stop_publishing()

if __name__ == '__main__':
    client=Client()
    loop=asyncio.get_event_loop()
    #print(id(client))
    task=loop.create_task(client.run())
    #loop.create_task(client.stop_publishing())
    loop.run_until_complete(asyncio.gather(task))
