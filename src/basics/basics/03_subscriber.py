import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class My_subscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber33')

        # Instanciating a subscriptor
        self.sub_ = self.create_subscription(String, 'my_topic33', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(msg.data)

def main():
    rclpy.init()

    my_subscriber = My_subscriber()
    rclpy.spin(my_subscriber)

    rclpy.shutdown()
