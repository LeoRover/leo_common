from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="cmd_vel_out",
                default_value="cmd_vel",
                description="Topic to send velocity commands on",
            ),
            Node(
                name="key_teleop",
                package="teleop_twist_keyboard",
                executable="teleop_twist_keyboard",
                output="screen",
                prefix="xterm -e",
                parameters=[
                    {
                        "speed": 0.4,
                        "turn": 1.0,
                        "repeat_rate": 10.0,
                        "key_timeout": 0.3,
                    }
                ],
                remappings={"cmd_vel": LaunchConfiguration("cmd_vel_out")}.items(),
            ),
        ]
    )
