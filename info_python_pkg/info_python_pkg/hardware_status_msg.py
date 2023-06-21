import rclpy 
from rclpy.node import Node

from test_interfaces.msg import HardwareStatus

class HardwareStatusPublisher(Node):

    def __init__(self):
        super().__init__("my_msg_node")
        self.publisher = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer = self.create_timer(3, self.publish_number)

    def publish_number(self):
        msg = HardwareStatus()
        msg.temprature = 45
        msg.are_motors_ready = True
        msg.debug_message = "HI"
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
