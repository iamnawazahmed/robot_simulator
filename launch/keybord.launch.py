import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_dir =get_package_share_directory('robot_simulator')
    

    ld = LaunchDescription()



    driving_node = Node(package='robot_simulator',executable='teleop_twist_keyboard',name='teleop_twist_keyboard',output='screen')

    ld.add_action(driving_node)

    return ld
