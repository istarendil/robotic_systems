from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    description = LaunchDescription()

    # Open URDF file
    share_dir_path = get_package_share_directory('scara')
    urdf_name = 'scara.urdf.xml'
    urdf_path = os.path.join(share_dir_path, urdf_name)
    with open(urdf_path, 'r') as my_file:
        robot_description = my_file.read()

    # Nodes
    rviz2_node = Node(package = 'rviz2',
                      executable = 'rviz2',
                      arguments = ['-d' + os.path.join(share_dir_path, 'scara_rviz_config.rviz')])

    state_publisher_node = Node(package = 'robot_state_publisher',
                                executable = 'robot_state_publisher',
                                output = 'screen',
                                arguments = [urdf_path],
                                parameters = [{'use_sim_time': False}, {'robot_description':robot_description}])

    joint_publisher_node = Node(package = 'scara',
                                executable = 'scara_joint_publisher',
                                output = 'screen')

    pendant_node = Node(package = 'scara',                
                        executable = 'virtual_pendant',
                        output = 'screen')

    trajectory_generator_node = Node(package = 'scara',                
                                     executable = 'trajectory_generator',
                                     output = 'screen')

    #joint_publisher_node = Node(package = 'joint_state_publisher_gui',
    #                            executable = 'joint_state_publisher_gui',
    #                            output = 'screen')

    # Add the nodes to the description
    description.add_action(rviz2_node)
    description.add_action(state_publisher_node)
    description.add_action(joint_publisher_node)
    description.add_action(pendant_node)
    description.add_action(trajectory_generator_node)

    return description

