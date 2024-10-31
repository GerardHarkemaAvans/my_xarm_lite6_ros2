from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rviz2',
            #namespace='rviz2',
            executable='rviz2',
            name='rviz'
        )
    ])


# <param name="robot_description" command="$(find xacro)/xacro '$(find my_lite6_description)/urdf/lite6_robot.urdf.xacro'" />
#  <node name="joint_state_publisher_gui" pkg="joint_state_publisher_gui" type="joint_state_publisher_gui">
#    <param name="use_gui" value="true" />
#  </node>
#  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
#  <node name="rviz" pkg="rviz" type="rviz" args="-d $(find my_lite6_description)/cfg/view_robot.rviz" required="true" />
