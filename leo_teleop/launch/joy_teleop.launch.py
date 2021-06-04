from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory("leo_teleop")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="joy_dev_id",
                default_value="0",
                description="Joystick device id",
            ),
            DeclareLaunchArgument(
                name="cmd_vel_out",
                default_value="cmd_vel",
                description="Topic to send velocity commands on",
            ),
            DeclareLaunchArgument(
                name="joy_config_file",
                default_value=pkg_share + "/config/joy_config.yaml",
                description="Path to the yaml file with parameters for joy_teleop_node",
            ),
            Node(
                name="joy_node",
                package="joy",
                executable="joy_node",
                parameters=[
                    {
                        "device_id": LaunchConfiguration("joy_dev_id"),
                        "coalesce_interval_ms": 50,
                        "autorepeat_rate": 10.0,
                    }
                ],
            ),
            Node(
                name="joy_teleop_node",
                package="teleop_twist_joy",
                executable="teleop_node",
                parameters=[LaunchConfiguration("joy_config_file")],
                remappings={"cmd_vel": LaunchConfiguration("cmd_vel_out")}.items(),
            ),
        ]
    )
