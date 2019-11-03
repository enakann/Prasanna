from joy_evaluation_node import Override
from multiprocessing import Process
from time import sleep
from threading import Thread
from fn_testframework.utils.threadwrapper import ThreadWrapper

p1=ThreadWrapper(Override('acc'),'run')
p1.daemon=True
p1.start()
sleep(10)
#import pdb;pdb.set_trace()
p1.stop()

