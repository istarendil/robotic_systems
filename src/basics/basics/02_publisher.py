import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class My_publisher(Node):
    def __init__(self):
        super().__init__('my_publisher')

        # Instanciating the publisher
        self.publisher_ = self.create_publisher(String, 'my_topic33', 10)
        self.timer_ = self.create_timer(0.5, self.publish)
        self.get_logger().info('Publisher started...')

    # Callback function
    def publish(self):
        my_msg = String()
        my_msg.data = 'ROS publishing...'
        self.publisher_.publish(my_msg)
        return

def main():
    rclpy.init()

    my_node = My_publisher()
    rclpy.spin(my_node)

    rclpy.shutdown()
