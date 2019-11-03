import threading
import time
import traceback
from collections import OrderedDict
import json

class Worker(threading.Thread):

    def __init__(self,obj,methodName,*args):
        super(Worker, self).__init__()
        self.obj=obj
        self.methodName=methodName
        self.args=args
        self.result=None
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        #self.join()

    def stopped(self):
        return self._stop_event.is_set()


    def run(self):
        print('In %s' % self.name)
        try:
            while not self.stopped():
                getattr(self.obj, self.methodName)(*self.args)
        except Exception as e:
            errorStack = traceback.format_exc()
            print(errorStack)

    def get_result(self):
        return self.result

    def getObject(self):
        return self.obj

    def getMethodName(self):
        return self.methodName

    def getName(self):
        return self.name

    def __str__(self):
        return "tid: " + self.getName() + ", object: " + str(self.getObject()) + ", method: " + self.getMethodName()


class MyEvalNode:
    def __init__(self):
        #super().__init__()
        self.logged_data=OrderedDict()
        self.logged_data['ego_long_vel'] = 0
        self.logged_data['ego_length'] = 0
        self.logged_data['breadth'] = 0
        self.logged_data['position_ego_x'] = 0
        self.logged_data['position_ego_y'] = 0
        self.logged_data['ego_lane_curvature'] = 0
        self.logged_data['max_acceleration'] = 0
        self.logged_data['max_deceleration'] = 0
        self.f=open("temp.text","w")


    def work(self):
        for i in range(1):
            for i, j in self.logged_data.items():
                self.logged_data[i] = j + 1
                self.f.write(json.dumps(self.logged_data))
                self.f.write("\n")
                self.f.write("################## "+ str(j) +"################")
                self.f.write("\n")
        return self.logged_data


if __name__ == '__main__':
    node = MyEvalNode()
    t1 = Worker(node, 'work')
    print(t1)
    t1.start()
    print(t1.is_alive())
    time.sleep(3)
    t1.stop()
    print(t1.is_alive())