#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_ip = LaunchConfiguration('robot_ip', default='192.168.2.162')
    hw_ns = LaunchConfiguration('hw_ns', default='ufactory')
    report_type = LaunchConfiguration('report_type', default='normal')
    prefix = LaunchConfiguration('prefix', default='')
    limited = LaunchConfiguration('limited', default=False)
    effort_control = LaunchConfiguration('effort_control', default=False)
    velocity_control = LaunchConfiguration('velocity_control', default=False)
    add_gripper = LaunchConfiguration('add_gripper', default=False)
    add_vacuum_gripper = LaunchConfiguration('add_vacuum_gripper', default=False)
    
    robot_ros2_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_controller'), 'launch', '_robot_ros2_control.launch.py'])),
        launch_arguments={
            'robot_ip': robot_ip,
            'report_type': report_type,
            'prefix': prefix,
            'hw_ns': hw_ns,
            'limited': limited,
            'effort_control': effort_control,
            'velocity_control': velocity_control,
            'add_gripper': add_gripper,
            'add_vacuum_gripper': add_vacuum_gripper,
            #'dof': '6',
            #'robot_type': 'lite',
            #'add_realsense_d435i': add_realsense_d435i,
            #'add_other_geometry': add_other_geometry,
            #'geometry_type': geometry_type,
            #'geometry_mass': geometry_mass,
            #'geometry_height': geometry_height,
            #'geometry_radius': geometry_radius,
            #'geometry_length': geometry_length,
            #'geometry_width': geometry_width,
            #'geometry_mesh_filename': geometry_mesh_filename,
            #'geometry_mesh_origin_xyz': geometry_mesh_origin_xyz,
            #'geometry_mesh_origin_rpy': geometry_mesh_origin_rpy,
            #'geometry_mesh_tcp_xyz': geometry_mesh_tcp_xyz,
            #'geometry_mesh_tcp_rpy': geometry_mesh_tcp_rpy,
        }.items(),
    )


    # robot moveit realmove launch
    # xarm_moveit_config/launch/_robot_moveit_realmove.launch.py
    #robot_moveit_realmove_launch = IncludeLaunchDescription(
    #    PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_moveit_config'), 'launch', '_robot_moveit_realmove.launch.py'])),
    #    launch_arguments={
    #        'robot_ip': robot_ip,
    #        'dof': '6',
    #        'robot_type': 'lite',
    #        'hw_ns': hw_ns,
    #        'no_gui_ctrl': 'false',
    #    }.items(),
    #)
    
    return LaunchDescription([
        robot_ros2_control_launch
        #robot_moveit_realmove_launch
    ])
