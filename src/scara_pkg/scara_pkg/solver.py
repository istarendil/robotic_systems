#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Interfaces
from scara_interfaces.srv import IkSolver

# Python modules
import numpy as np
import transforms3d 

# Inverse-kinematics-solver for a Scara robot
class Solver(Node):
    def __init__(self, a1, a2, d1, d4):
        # Node's name
        super().__init__('scara_solver')

        # Robot parameters
        self.__a1 = a1
        self.__a2 = a2
        self.__d1 = d1
        self.__d4 = d4

        # Service definition
        self.srv = self.create_service(IkSolver, 'scara_ik', self.callback)
        self.get_logger().info('Scara: Ik-solver ready...')


    def callback(self, request, response):
        # Get the request data
        position = request.pose.position
        quat = request.pose.orientation

        # Convert quaternion to Euler( extrinsic zyx)
        orientation = transforms3d.euler.quat2euler([quat.w, quat.x, quat.y, quat.z], 'szyx')
        alpha = orientation[0]

        # Inverse-kinematics computing
        q = self.ik(position.x, position.y, position.z, alpha)

        # Response
        response.names = ['q1', 'q2', 'q3','q4']
        response.positions = q 

        return response

    def ik(self, Ox, Oy, Oz, alpha):
        D = (Ox**2 + Oy**2 - self.__a1**2 - self.__a2**2)/(2*self.__a1*self.__a2)
        
        d3 = self.__d1 - self.__d4 - Oz
        th2 = np.arctan2(np.sqrt(1 - D**2), D)
        th1 = np.arctan2(Oy, Ox) - np.arctan2(self.__a2*np.sin(th2), self.__a1 + self.__a2*np.cos(th2))
        th4 = th1 + th2 -alpha
        
        return [th1, th2, d3, th4]


def main(args=None):
    rclpy.init(args=args)

    try:
        solver = Solver(0.5, 0.5, 1.0, 0.2)
        rclpy.spin(solver)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

