#!/usr/bin/env python3

# ROS packages
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectoryPoint
from scara_interfaces.srv import Tracer 

import numpy as np

# Node
class ScaraTracer(Node):
    def __init__(self):
        super().__init__('scara_tracer')
        
        # Service definition
        self.srv = self.create_service(Tracer, 'scara_trajectory', self.callback)
        self.get_logger().info('Scara tracer ready...')

        self.trajPoint = JointTrajectoryPoint()

    def callback(self, request, response):
        # Get the request data
        q0 = request.initial_point.positions
        v0 = request.initial_point.velocities
        
        qf = request.final_point.positions
        vf = request.final_point.velocities
        tf = request.final_point.time_from_start.sec

        # Generate the trajectory
        a, v, q, t = self.jTraj3(self, tf, q0, qf, v0, vf) 

        # Sort the response data
        trajectory = []
        for i in range(q.shape[0]):
            self.trajPoint.positions = q[i, :]
            self.trajPoint.velocities = v[i, :]
            self.trajPoint.accelerations = a[i, :]
            self.trajPoint.time_from_start = t[i]

            points.append(self.trajPoint)

        # Response
        now = self.get_clock().now()
        response.header.stamp = now.to_msg()
        response.joint_names = ['q0', 'q1', 'q2', 'q3']
        response.points = trajectory 

        return response
        
    def jTraj3(self, tf, q0, qf, v0, vf):
        # Time step
        dt = 1/50
        
        # Time vector
        t = np.arange(0, tf+dt, dt)

        # Polynomia coefficients
        C0 = q0
        C1 = v0
        C2 = (3*(qf - q0)/tf**2) - ((vf + 2*v0)/tf)
        C3 = -(2*(qf -q0)/tf**3) + ((vf + v0)/tf**2)

        # Resulting trajectories
        q = np.dot(np.array([t**0, t, t**2, t**3]).transpose(), np.array([C0, C1, C2, C3]))
        v = np.dot(np.array([t**0, t, t**2]).transpose(), np.array([C1, 2*C2, 3*C3]))
        a = np.dot(np.array([t**0, t]).transpose(), np.array([2*C2, 6*C3]))

        return a, v, q, t

def main():
    rclpy.init()
    try:
        tracer = ScaraTracer()
        rclpy.spin(tracer)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__=='__main__':
    main()
