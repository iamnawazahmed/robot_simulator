import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_dir =get_package_share_directory('robot_simulator')
    world_files = os.path.join(package_dir,'worlds','car.world')

    ld = LaunchDescription()

    gazeboworld = ExecuteProcess(
        cmd=['gazebo','--verbose',world_files,'-s','libgazebo_ros_factory.so']
    )

    driving_node = Node(package='robot_simulator',executable='driving_node',name='driving_node',output='screen')

    ld.add_action(gazeboworld)
    ld.add_action(driving_node)

    return ld
