import rclpy
import threading
import time
from std_msgs.msg import String
from weakref import WeakValueDictionary
import subprocess
class Singleton(type):
    _instance=WeakValueDictionary()
    def __call__(self,*args,**kwargs):
        if not self in self._instance:
            self._instance[self]=super().__call__(*args,**kwargs)
        return self._instance[self]

rclpy.init(args=None)

class Driver(metaclass=Singleton):
    def __init__(self,a):
        self.a=a
        print("Init called with {}".format(self.a))
        #rclpy.init(args=None)
        self.driver_control=rclpy.create_node("driver_control")
        self.publisher=self.driver_control.create_publisher(String,"/test/topic")
        self.state=True
        self.t1=threading.Thread(target=self.publish,args=(),daemon=False)


    def publish(self):
        i=self.a
        msg=String()
        while self.state:
            msg.data="hello "+str(self)+"  " + str(i)
            self.publisher.publish(msg)
            print(msg.data)
            i+=1
            time.sleep(0.5)

    def start_publishing(self):
        self.t1.start()

    def stop_publishing(self):
        self.state=False
        self.t1.join()
        self.driver_control.destroy_node()

    def __str__(self):
        return str(self.a)

def get_nodes(cmd):
    print(cmd)
    print(subprocess.call(['ros2','node', 'list']))

if __name__ == '__main__':
    for i in [10,20] :
        obj=Driver(i)
        obj.start_publishing()
        time.sleep(2)
        get_nodes("before stopping")
        obj.stop_publishing()
        del obj
        time.sleep(1)
        get_nodes("after stopping")
