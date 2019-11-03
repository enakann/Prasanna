import os
import subprocess
from ros2_poc.ros_poc import Client
from ros2_poc.ros_poc import Consumer
from contextlib import contextmanager
from time import sleep
from multiprocessing import Process
@contextmanager
def override(feature,joy=None):
    os.environ['OVERRIDE'] = 'LCC'
    obj=Client()
    p=subprocess.Popen(['python','ros_poc.py'])
    yield obj.get_overrideobj()
    p.wait()
    p.terminate()


with override("ACC",'joy') as over:
    print(id(over))
    for i in range(5):
        over.break_override()
        sleep(1)
    print("Testing will be done here ")

