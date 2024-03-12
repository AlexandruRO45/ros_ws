#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import Empty
import baxter_interface


class PickAndPlaceMoveIt:
    def __init__(self, limb, hover_distance=0.15, verbose=True):
        """
        Initialize the Pick and Place operation using Baxter and MoveIt.

        Args:
            limb (str): The limb to use ('left' or 'right').
            hover_distance (float): Distance to hover above target before and after pick/place.
            verbose (bool): Enable verbose output for debugging.
        """

        self.limb_name = limb
        self.hover_distance = hover_distance
        self.verbose = verbose
        self.limb = baxter_interface.Limb(limb)
        self.gripper = baxter_interface.Gripper(limb)


         # Enable the robot and initialize required interfaces
        print("Enabling robot... ")
        rs = baxter_interface.RobotEnable(baxter_interface.CHECK_VERSION)
        self.init_state = rs.state().enabled

        self.robot = moveit_commander.RobotCommander()
        self.group = moveit_commander.MoveGroupCommander("{}_arm".format(limb))


    def move_to_start(self, start_pose):
        """Moves the arm to the starting pose."""
        print("Moving the {} arm to start pose...".format(self.limb_name))
        self.gripper_open()
        self.set_target_and_move(start_pose)
        rospy.sleep(1.0)
        print("Running. Ctrl-c to quit")

    def set_target_and_move(self, pose):
        """Sets the target pose and moves the arm."""
        self.group.set_pose_target(pose)
        plan = self.group.plan()
        self.group.execute(plan)

    def gripper_open(self):
        """Opens the gripper."""
        self.gripper.open()
        rospy.sleep(1.0)

    def gripper_close(self):
        """Closes the gripper."""
        self.gripper.close()
        rospy.sleep(1.0)

    def approach(self, pose):
        """Approaches the given pose."""
        approach_pose = copy.deepcopy(pose)
        approach_pose.position.z += self.hover_distance
        self.set_target_and_move(approach_pose)

    def retract(self):
        """Retracts the arm from the target."""
        current_pose = self.limb.endpoint_pose()
        retract_pose = Pose(
            position=Point(
                x=current_pose['position'].x,
                y=current_pose['position'].y,
                z=current_pose['position'].z + self.hover_distance),
            orientation=current_pose['orientation'])
        self.set_target_and_move(retract_pose)

    def pick(self, pose):
        """Performs the pick operation."""
        self.gripper_open()
        self.approach(pose)
        self.set_target_and_move(pose)  # Move to the exact pose
        self.gripper_close()
        self.retract()

    def place(self, pose):
        """Performs the place operation."""
        self.approach(pose)
        self.set_target_and_move(pose)  # Move to the exact pose
        self.gripper_open()
        self.retract()

def prepare_poses(orientation, position_map, pick_list):
    """Prepares a list of poses based on specified pick positions."""
    return [
        Pose(
            position=Point(
                    x=position[0], 
                    y=position[1], 
                    z=position[2]
                ), 
            orientation=orientation
        ) for position in (position_map[pick] for pick in pick_list)
    ]

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("ik_pick_and_place_moveit")
    rospy.wait_for_message("/robot/sim/started", Empty)

    limb = 'left'
    overhead_orientation = Quaternion(
        x=-0.0249590815779, y=0.999649402929,
        z=0.00737916180073, w=0.00486450832011)
    starting_pose = Pose(position=Point(x=0.7, y=0.135, z=0.35), orientation=overhead_orientation)

    pnp = PickAndPlaceMoveIt(limb)
    position_map = rospy.get_param('piece_target_position_map')

    pick_list = ['00', '70', '20']
    place_list = ['04', '50', '21']

    pick_block_poses = prepare_poses(overhead_orientation, position_map, pick_list)
    place_block_poses = prepare_poses(overhead_orientation, position_map, place_list)


    pnp.move_to_start(starting_pose)


    for pick_pose, place_pose in zip(pick_block_poses, place_block_poses):
        print("\nPicking...")
        pnp.pick(pick_pose)
        print("\nPlacing...")
        pnp.place(place_pose)

    return 0


if __name__ == '__main__':
    sys.exit(main())