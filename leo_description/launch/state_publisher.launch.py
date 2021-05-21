from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('leo_description')

    return LaunchDescription([
        DeclareLaunchArgument(
            name='model',
            default_value=pkg_share + '/urdf/leo.urdf.xacro',
            description='Absolute path to robot urdf.xacro file'
        ),
        Node(
            name="robot_state_publisher",
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                 'robot_description': Command(['xacro ', LaunchConfiguration('model')])
            }],
        )
    ])
