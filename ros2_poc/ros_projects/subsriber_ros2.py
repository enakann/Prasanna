import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Drive(Node):
    def __init__(self):
        super().__init__('drive')

        self.sub_image = self.create_subscription(String, '/test/topic', self.callback)

    def callback(self, msg):
        #self.get_logger().info('Subscribed: {}'.format(msg.data))
        print(msg.data)


def main(args=None):
    rclpy.init(args=args)
    drive = Drive()
    rclpy.spin(drive)


if __name__ == '__main__':
    main()
