import rclpy 
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class ServiceClient(Node):

    def __init__(self):
        super().__init__("service_client")
        self.call_service_server(3,5)

    def call_service_server(self,a,b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_done, a =a, b=b))

    def callback_done(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a)+" + "+str(b)+" = "+str(response.sum))
        except Exception as e:
            self.get_logger().error(e)


def main(args=None):
    rclpy.init(args=args)
    node = ServiceClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
