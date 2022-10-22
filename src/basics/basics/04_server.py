import rclpy
from rclpy.node import Node
from basic_interfaces.srv import MySrv

class Server(Node):
    def __init__(self):
        super().__init__('my_server')
        self.my_log = self.get_logger()

        # Instanciating a server
        self.srv_ = self.create_service(MySrv, 'my_service', self.callback)
        self.my_log.info('server initialized...')

    def callback(self, request, response):
        response.c = request.a + request.b
        return response

        
def main():
    rclpy.init()

    while rclpy.ok():
        # Instanciating a server
        my_server = Server()
        # Spining the server
        rclpy.spin(my_server)
    
    rclpy.shutdown()
    
    
if __name__=='__main__':
    main()
    
