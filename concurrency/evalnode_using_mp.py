import os
import time
from data_logger import DataLogger
from mythread import Worker
#from mymultiprocessing import Worker
from collections import OrderedDict
from multiprocessing import Lock,Manager
import json
lock=Lock()

PATH_LOG="./log"

class EvalNode:
    def __init__(self):
        self.logged_data = OrderedDict({'time_stamp': 0})
        #self.create_data_logger_instance()
        self.t1=Worker(self,'time_synched_cb')
        self.__message=''


    def create_data_logger_instance(self):
        """Create the DataLogger class instance for logging the data."""
        self.__data_log_path = os.path.join(PATH_LOG, time.strftime("%Y-%m-%d_%H%M%S") + "_log")
        if not os.path.exists(self.__data_log_path):
            os.makedirs(self.__data_log_path)
        self.data_logger = DataLogger('data_log.csv', self.__data_log_path, 'plot.png')

    def trigger_test(self,cmd):
        if cmd=='start':
            if self.t1.is_alive():
                self.__message = "{} is already running.".format(self.t1)
            else:
                self.t1.start()
                self.__message = "{} is started".format(self.t1)
        elif cmd=='stop':
            if not self.t1.is_alive():
                self.__message = "{} is already stopped".format(self.t1)
            else:
                self.t1.stop()
                self.data_logger.save_data_to_csv()
                self.__message = "{} is stopped".format(self.t1)
        print(self.__message)
        return self.__message

    def log_to_datafile_and_dcrt(self):
        """Return dcrt debug message and adds data to data list."""
        now = self.timestamp()
        self.logged_data['time_stamp'] = '%d' % (now)
        print(self.logged_data)
        message = self.data_logger.create_dcrt_log_message(now, self.logged_data)
        self.data_logger.add_data_to_data_list(self.logged_data)
        return message

    def time_synched_cb(self):
        """Call back function for SCP Receive thread."""
        message_dat = self.log_to_datafile_and_dcrt()
        #print(message_dat)
        time.sleep(0.005)

    def timestamp(self):
        """Return the current clock time."""
        return time.time()


class MyEvalNode(EvalNode):
    def __init__(self):
        super().__init__()
        self.logged_data['ego_long_vel'] = 0
        self.logged_data['ego_length'] = 0
        self.logged_data['breadth'] = 0
        self.logged_data['position_ego_x'] = 0
        self.logged_data['position_ego_y'] = 0
        self.logged_data['ego_lane_curvature'] = 0
        self.logged_data['max_acceleration'] = 0
        self.logged_data['max_deceleration'] = 0


    def work(self):
        for i, j in self.logged_data.items():
            if not i == 'time_stamp':
                with lock:
                    self.logged_data[i] = j + 1
                #print(self.logged_data)
            #time.sleep(0.5)


if __name__ == '__main__':
    node=MyEvalNode()
    node.create_data_logger_instance()
    t1=Worker(node,'work')
    print(t1)
    t1.start()
    node.trigger_test('start')
    print("sleep started")
    time.sleep(10)
    print("sleep stopped")

    print(t1.is_alive())
    print(node.t1.is_alive())

    t1.stop()
    node.trigger_test('stop')

    print(t1.is_alive())
    print(node.t1.is_alive())

