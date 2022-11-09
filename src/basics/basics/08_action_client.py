import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from basic_interfaces.action import MyAction

class ActionClientNode(Node):
    def __init__(self):
        super().__init__('my_action_client')

        # Instanciate an action client
        self.client_ = ActionClient(self, MyAction, 'my_action_service')

    def request_service(self, position):
        # Instanciate a goal message
        goal = MyAction.Goal()
        goal.goal_position = position

        # Wait to the server
        self.client_.wait_for_server()

        # Send the request and get a handler
        self.request_handler = self.client_.send_goal_async(goal, feedback_callback = self.feedback_callback)

        # Associate a callback with the request_handler
        self.request_handler.add_done_callback(self.request_callback)

    def request_callback(self, request_handler):
        # Check if the reuest has been accepted
        if not request_handler.result().accepted:
            self.get_logger().info('Request regected..')
            return
        else:
            self.get_logger().info('Request accepted...')

        # Request the action-service result and get a handler
        self.result_handler = request_handler.result().get_result_async()

        # Associate a callback with the result_handler
        self.result_handler.add_done_callback(self.result_callback)

    def result_callback(self, result_handler):
        # Read the result
        result = result_handler.result().result
        self.get_logger().info(f'Result: {result.result_position}')

        # Shutdown the client
        rclpy.shutdown()

    def feedback_callback(self, feedback_handler):
        self.get_logger().info(f'Feedback: {feedback_handler.feedback.current_position}')


def main():
    rclpy.init()
    action_client = ActionClientNode()

    action_client.request_service([3, 5, 8])
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
