import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class move_node(Node):

    def __init__(self):
        super().__init__('move_custom_Node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = move_node()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()