# ROS Workspace (Melodic)

This repository contains a ROS workspace with several packages for a good understanding in robotics foundation. 

## Packages

The workspace contains the following packages:

* **camera_calibration**: Contains tools for calibrating cameras.
* **image_processing**: Contains tools for processing images.
* **navigation**: Contains tools for robot navigation.
* **perception**: Contains tools for object detection and recognition.
* **planning**: Contains tools for path planning.
* **robot_control**: Contains tools for controlling robots.
* **simulation**: Contains tools for simulating robots and environments.

The rf_ws folder contains all the practical labs to get started with baxter:
* **baxter_chess**:
* **lab1_pkg**:
* **lab2_pkg**:
* **lab3_pkg**:
* **lab4_pkg**:
* **lab5_pkg**:

## Installation

To install the workspace, clone it to your designated location. The virtual machine to run the workspace can be found here.

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

The can be included at the end if the file by using (vim/nano or any other editing tool):
```
nano ~/.bashrc
```

Then, you can use the packages as usual. For example, to launch the chess pick and place game, run:

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
rosrun baxter_chess pick_and_plave_moveit.py
```
### Terminal 6:
```
rosrun baxter_chess gazebo2tfframe.py
```

In order to delete the chessboard and its components, run the command:
```
rosrun baxter_chess delete_chessgame_h.py
```


## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
