## How to play chess with baxter
Clone the repository, run `catkin_make` and source your workspace.  
Run the following in separate terminals:

Terminal 1:
```
roslaunch baxter_gazebo baxter_world.launch
```
Terminal 2:
```
rosrun baxter_tools enable_robot.py -e
rosrun baxter_interface joint_trajectory_action_server.py
```
Terminal 3:
```
roslaunch baxter_moveit_config baxter_grippers.launch
```
Terminal 4:
```
rosrun chess_baxter spawn_chessboard.py
```
Terminal 5:
```
rosrun chess_baxter pick_and_plave_moveit.py
```
Terminal 6:
```
rosrun chess_baxter gazebo2tfframe.py
```

In order to delete the chessboard and its components once you done, run the command:
```
rosrun chess_baxter delete_chessgame.py
```