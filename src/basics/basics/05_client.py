import rclpy
from rclpy.node import Node
from basic_interfaces.srv import MySrv

class Client(Node):
    def __init__(self):
        super().__init__('my_client')
        self.logger_ = self.get_logger()

        # Instanciating a client
        self.client_ = self.create_client(MySrv, 'my_service')
        self.logger_.info('Client initialized...')

        # Wait for the server
        while not self.client_.wait_for_service(timeout_sec = 1):
            pass

        # Instanciating a request-object
        self.req = MySrv.Request()

    def request(self, a, b):
        self.req.a = a
        self.req.b = b

        # Call the server
        self.response_ = self.client_.call_async(self.req)

        
def main():
    rclpy.init()

    # Instanciating a client 
    my_client = Client()
    # Make the request
    my_client.request(7, 3)
    # Spin the node
    rclpy.spin_once(my_client)

    # Check if the response is ready
    if my_client.response_.done():
        result_ = my_client.response_.result()
        my_client.logger_.info(f'Result: {result_.c}')
    
    rclpy.shutdown()
    
    
if __name__=='__main__':
    main()
    
