import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

PACKAGE_NAME = 'umrr_ros2_driver'

def generate_launch_description():
    # Launch-Argument deklarieren
    param_file_arg = DeclareLaunchArgument(
        'param_file',
        default_value=os.path.join(
            get_package_share_directory(PACKAGE_NAME),
            'param/radar.params.template.yaml'
        ),
        description='Path to radar node parameter file'
    )

    # LaunchConfiguration verwenden
    radar_node = Node(
        package=PACKAGE_NAME,
        executable='smartmicro_radar_node_exe',
        name='smart_radar',
        parameters=[LaunchConfiguration('param_file')]
    )

    return LaunchDescription([
        param_file_arg,
        radar_node
    ])