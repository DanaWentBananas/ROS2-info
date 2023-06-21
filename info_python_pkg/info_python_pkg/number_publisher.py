import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int64

class NumberPublisher(Node):

    def __init__(self):
        super().__init__("number_publisher_node")
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.timer = self.create_timer(3, self.publish_number)
        self.declare_parameter("number",3)

    def publish_number(self):
        num = self.get_parameter("number").value
        msg = Int64()
        msg.data = num
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
