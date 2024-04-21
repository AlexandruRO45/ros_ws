# ROS Workspace (Melodic)

This repository contains a ROS workspace with several packages to understand the robotics foundation better (experimenting with the simulated robot, Baxter). 

## Packages

The workspace contains the following packages:

* **Gazebo Simulator**: 3D robotics simulator that provides a physics engine, high-quality graphics, and a plugin architecture for robot simulation.
* **RViz**: a visualization tool for ROS that allows you to visualize sensor data, robot models, and the environment, useful for debugging and understanding robot behaviour.
* **MoveIt!**: ROS framework for motion planning, manipulation, and control, providing tools for kinematics, collision checking, and visualization.
* **OMPL (Open Motion Planning Library)**: powerful library for motion planning, providing implementations of various motion planning algorithms. 
* **ROS Control**: a set of ROS packages that provide tools for controlling robot joints and interfaces with hardware drivers.



The rf_ws folder contains all the practical labs to get started with Baxter:
* **baxter_chess**: Testing the ability of Baxter to move chess pieces on the chessboard. 
* **lab1_pkg**: Exploring the simulation facilities in ROS and navigating Baxter's arms using keyboard arrows.
* **lab2_pkg**: Learn how ROS handles coordinate transformations and discover the Unified Robot Description Format (URDF) and XML macros (aka XACRO). 
* **lab3_pkg**: Using the ROS motion planning framework, Moveit to discover planning algorithms via the Open Motion Planning Library (OMPL).
* **lab4_pkg**: Application of the framework for locating an object, grasping it and placing it in another location.
* **lab5_pkg**: Visualisation camera using a depth sensor to detect blocks and pick/place them around the environment. 


## Installation

To install the workspace, clone it to your designated location. To facilitate easy setup and usage of the ROS workspace (as Melodic reached the EOL date), you can download a pre-configured virtual machine (VM) image for VirtualBox. This VM includes all the necessary software and packages to run the ROS environment and experiment with the provided repository.

### Download Link:

[ROS Melodic Virtual Machine Image](https://drive.google.com/drive/folders/1-asjY5BQOW_zEhT6_00lPzvrY0FAn9ux?usp=sharing)

Build the workspace only after deleting build, devel and install folders for a fresh install or if you do not use the virtual machine provided:

```
cd ~/ros_ws
catkin_make & catkin_make install
```

## Usage

To use the packages in the workspace, source the setup file:

```
source ~/ros_ws/devel/setup.bash
```
Or:

It's always a good practice to set the setup files inside the ~/.bashrc to avoid sourcing all the time.
Example:
```
source /opt/ros/melodic/setup.bash
PATH="${HOME}/.local/bin:$PATH"
source ~/ros_ws/devel/setup.bash
source ~/ros_ws/rf_ws/devel/setup.bash
```

They can be included at the end of the file by using (vim/nano or any other editing tool):
```
nano ~/.bashrc
```

Then, you are free to use the packages as usual. 

To launch the chess pick and place game, run (give a 10-30 seconds delay between commands to allow them to be properly configured):

### Terminal 1:
```
roslaunch baxter_gazebo baxter_world.launch
```
### Terminal 2:
```
rosrun baxter_tools enable_robot.py -e
rosrun baxter_interface joint_trajectory_action_server.py
```
### Terminal 3:
```
roslaunch baxter_moveit_config baxter_grippers.launch
```
### Terminal 4:
```
rosrun baxter_chess spawn_chessboard_h.py
```
### Terminal 5:
```
rosrun baxter_chess pick_and_place_moveit.py
```
### Terminal 6:
```
rosrun baxter_chess gazebo2tfframe.py
```

To delete the chessboard and its components, run the command:
```
rosrun baxter_chess delete_chessgame_h.py
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
