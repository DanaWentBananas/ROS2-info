import rclpy 
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsNode(Node):

    def __init__(self):
        super().__init__("add_two_ints")
        self.server = self.create_service(
            AddTwoInts, "add_two_ints", self.callback
        )
        self.get_logger().info("Server has started")

    def callback(self,request,response):
        response.sum = request.a + request.b
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
