import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int64

from example_interfaces.srv import SetBool

class NumberCounter(Node):

    def __init__(self):
        super().__init__("number_counter_node")
        self.counter = 0
        self.subscriber = self.create_subscription(Int64, "number", self.sub_callback,10)
        self.publisher = self.create_publisher(Int64, "number_count", 10)

        self.server = self.create_service(SetBool, "reset_counter", self.server_callback)

    def sub_callback(self,msg):
        num = msg.data
        self.counter += num
        self.get_logger().info("Counter: "+str(self.counter))
        count_msg = Int64()
        count_msg.data = self.counter
        self.publisher.publish(count_msg)

    def server_callback(self,request,response):
        self.counter = 0
        response.message = "Counter has been reset"
        self.get_logger().info(str(request)+"   "+response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
