import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')

        
def main():
    rclpy.init()
    
    rclpy.shutdown()
    
    
if __name__=='__main__':
    main()
    
