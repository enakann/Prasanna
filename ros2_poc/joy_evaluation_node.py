import os
import threading
import time
from time import sleep
from collections import OrderedDict
from sensor_msgs.msg import Joy
from rclpy.node import Node
import rclpy
from visteon_vehicle_msgs.msg import VehicleReport
from fn_testframework.utils.threadwrapper import ThreadWrapper
import subprocess
from multiprocessing import Process


# create a node for subscription

class JoyNode(Node):
    """Base class for all test evaluation nodes. Implements all common methods for evaluation nodes."""
    #'throttle_override': 'int8',
    #'brake_override': 'int8'
    #'steering_override': 'int8'

    #'header': 'std_msgs/Header',
    #'axes': 'sequence<float>',
    #'buttons': 'sequence<int32>',

    def __init__(self, node_name):
        super().__init__(node_name)
        self.__eval_node_name = node_name
        self.create_subscription(Joy, "/joy", self.joy)
        self.__publishers=[]
        self.__thread=ThreadWrapper(self,'publish')
        self.__running=False
        self._frontbutton=None
        self._rightbutton=None
        self._backbutton=None
        self._leftbutton=None

    @property
    def frontbutton(self):
        return self._frontbutton

    @frontbutton.setter
    def frontbutton(self,val):
        #import pdb;pdb.set_trace()
        self._frontbutton = val
        if val:
            self.frontbuttonInteration()

    @property
    def rightbutton(self):
        return self._rightbutton

    @rightbutton.setter
    def rightbutton(self, val):
        self._rightbutton = val
        if val:
            self.rightbuttonInteration()


    @property
    def backbutton(self):
        return self._backbutton

    @backbutton.setter
    def backbutton(self,val):
        #import pdb;pdb.set_trace()
        self._backbutton = val
        if val:
            self.backbuttonInteration()

    @property
    def leftbutton(self):
        return self._leftbutton

    @leftbutton.setter
    def leftbutton(self, val):
        self._leftbutton = val
        if val:
            self.leftbuttonInteration()



    def joy(self,joy_msg):
        """
        #print("header ---> {}".format(joy_msg.header))
        #print("axes ---> {}".format(joy_msg.axes))
        #print("buttons ---> {}".format(joy_msg.buttons))
        :param joy_msg:
        :return:
        """
        #import pdb;pdb.set_trace()
        #print(self.msg.brake_override)
        #print(self.__thread.is_alive())

        self.frontbutton,self.rightbutton,self.backbutton,self.leftbutton,*args = joy_msg.buttons.tolist()
        x_left,x_right,y_left,y_right,*args = joy_msg.axes.tolist()

    def addpublisher(self,publisher):
        self.__publishers.append(publisher)

    def publish(self):
        cmd = 'ros2  topic pub /ex/vehicle/report visteon_vehicle_msgs/VehicleReport "{ brake_override : 1 }"'
        for publisher in self.__publishers:
            #print(self.msg)
            publisher.publish(self.msg)

    def start_publishing(self):
        self.__thread.start()


    def stop_publishing(self):
        self.__thread.stop()

class ACCOverride(JoyNode):
    topic="/ex/vehicle/report"
    msg=VehicleReport()

    def __init__(self,node_name):
        super().__init__(node_name)
        self.__publisher = self.create_publisher(VehicleReport, self.topic)
        self.addpublisher(self.__publisher)
        self.start_publishing()
        #self.brake_override()

    def brake_override(self):
        self.msg.brake_override = 1
        timer = threading.Timer(0.5,lambda: self.__reset_msg_field("brake_override"))
        timer.start()

    def throttle_override(self):
        self.msg.throttle_override = 1
        timer = threading.Timer(0.5, lambda: self.__reset_msg_field("throttle_override"))
        timer.start()

    def steering_override(self):
        self.msg.steering_override = 1
        timer = threading.Timer(0.5, lambda: self.__reset_msg_field("steering_override"))
        timer.start()

    def frontbuttonInteration(self):
        self.brake_override()

    def rightbuttonInteration(self):
        self.throttle_override()

    def backbuttonInteration(self):
        self.steering_override()

    def leftbuttonInteration(self):
        pass



    def __reset_msg_field(self, field_name):
        setattr(self.msg, field_name, 0)

    def __del__(self):
        self.stop_publishing()


class LCCoveride(JoyNode):
    topic = "/ex/vehicle/report"
    msg = VehicleReport()
    def __init__(self,node_name):
        super().__init__(node_name)
        self.__publisher = self.create_publisher(VehicleReport, self.topic)
        self.addpublisher(self.__publisher)
        self.start_publishing()


class Override:
    def __init__(self,override_type):
        self.override=override_type
        self.override_type_mapping={
            'acc':ACCOverride,
            'lcc':LCCoveride,
        }
        self.node=self.override_type_mapping.get(self.override)
        rclpy.init(args=None)


    def run(self):

        #import pdb;pdb.set_trace()
        NODE = self.node(self.node.__name__)
        try:
            #import pdb;pdb.set_trace()
            rclpy.spin(NODE)
        except KeyboardInterrupt as excep:
            NODE.destroy_node()
            rclpy.shutdown()

    def stop(self):
        self.node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    obj=Override('acc').run()
    sleep(5)
    obj.stop()

