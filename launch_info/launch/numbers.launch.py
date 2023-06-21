from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    remap_count_topic = ("number_count", "poop")

    number_pub_node = Node(
        package="test_pkg1",
        executable="number_publisher_x",
        name = "publisher_potato",
        remappings=[
            ("number","another_name_for_number")
        ],
        parameters=[
            {"number": 10}
        ]
    )

    counter_node = Node(
        package="test_pkg1",
        executable="number_counter_x",
        name = "counter_potato",
        remappings=[
            ("number","another_name_for_number"),
            remap_count_topic
        ]
    )

    ld.add_action(number_pub_node)
    ld.add_action(counter_node)

    return ld