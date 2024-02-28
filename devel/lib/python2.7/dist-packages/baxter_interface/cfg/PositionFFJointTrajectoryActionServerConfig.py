## *********************************************************
##
## File autogenerated for the baxter_interface package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Amount of time (s) controller is permitted to be late achieving goal', 'max': 120.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'goal_time', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Maximum velocity (m/s) at end of trajectory to be considered stopped', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'stopped_velocity_tolerance', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_s0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_s0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_s1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_s1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_e0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_e0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_e1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_e1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w2 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w2_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_s0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_s0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_s1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_s1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_e0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_e0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_e1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_e1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w0 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w0_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w1 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w1_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w2 - maximum final error', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w2_goal', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_s0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_s0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_s1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_s1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_e0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_e0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_e1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_e1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'left_w2 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'left_w2_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_s0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_s0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_s1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_s1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_e0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_e0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_e1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_e1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w0 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w0_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w1 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w1_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'right_w2 - maximum error during trajectory execution', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'right_w2_trajectory', 'edit_method': '', 'default': 0.35, 'level': 0, 'min': -1.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

