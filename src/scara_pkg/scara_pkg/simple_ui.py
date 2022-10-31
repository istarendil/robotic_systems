#/usr/bin/env python3

import rclpy
from rclpy.node import Node

from scara_interfaces.srv import IkSolver, Tracer
import transforms3d

class SimpleUi(Node):
    def __init__(self):
        super().__init__('simple_user_interface')

        self.solverClient = self.create_client(IkSolver, 'scara_ik')
        self.tracerClient = self.create_client(Tracer, 'scara_trajectory')
        self.get_logger().info('Simple_user_interface: Ready...')
        self.solverReq = IkSolver.Request()
        self.tracerReq = Tracer.Request()

        while not self.solverClient.wait_for_service(timeout_sec = 1.0):
            pass

    def request(self, position, orientation):
        self.solverReq.pose.position.x = position[0] 
        self.solverReq.pose.position.y = position[1]
        self.solverReq.pose.position.z = position[2]
        self.solverReq.pose.orientation.w = orientation[0]
        self.solverReq.pose.orientation.x = orientation[1]
        self.solverReq.pose.orientation.y = orientation[2]
        self.solverReq.pose.orientation.z = orientation[3]

        self.future = self.solverClient.call_async(self.solverReq)

def main(args=None):
    rclpy.init(args=args)

    my_ui = SimpleUi()
    
    # Quaternion
    quat = transforms3d.euler.euler2quat(0.7854, 0, 0, 'szyx')

    # Request
    my_ui.request((0.3, 0.7, 0.35), quat)
    rclpy.spin_once(my_ui)

    while not my_ui.future.done():
        pass

    try:
        response = my_ui.future.result()
        my_ui.get_logger().info(f'Names: {response.names}')
        my_ui.get_logger().info(f'Response: {response.positions}')
    except:
        pass

    my_ui.destroy_node()
    rclpy.shutdown()

