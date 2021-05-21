from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            name='key_teleop',
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            output='screen',
            prefix='xterm -e',
            parameters=[{
                'speed': 0.4,
                'turn': 1.0,
                'repeat_rate': 10.0,
                'key_timeout': 0.3,
            }]
        ),
    ])
