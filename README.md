# ROS Workspace

This repository contains a ROS workspace with several packages for different tasks.

## Packages

The workspace contains the following packages:

* **camera_calibration**: Contains tools for calibrating cameras.
* **image_processing**: Contains tools for processing images.
* **navigation**: Contains tools for robot navigation.
* **perception**: Contains tools for object detection and recognition.
* **planning**: Contains tools for path planning.
* **robot_control**: Contains tools for controlling robots.
* **simulation**: Contains tools for simulating robots and environments.

## Installation

To install the workspace, clone it into your catkin workspace:

```
cd ~/catkin_ws/src
git clone https://github.com/AlexandruRO45/ros_ws.git
```

Then, build the workspace:

```
cd ~/catkin_ws
catkin_make
```

## Usage

To use the packages in the workspace, source the setup file:

```
source ~/catkin_ws/devel/setup.bash
```

Then, you can use the packages as usual. For example, to launch the camera calibration tool, run:

```
roslaunch camera_calibration camera_calibration.launch
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
