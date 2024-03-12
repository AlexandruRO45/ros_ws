#!/usr/bin/env python
# Reference: http://wiki.ros.org/simulator_gazebo/Tutorials/ListOfMaterials
import sys
import rospy
import tf
import rospkg
from geometry_msgs.msg import Pose, Point, Quaternion
from copy import deepcopy
from pick_and_place_moveit import PickAndPlaceMoveIt
from gazebo_utils import load_model, spawn_model


def set_up_chess_pieces(pnp, board_pose, pieces_xml, board_setup, overhead_orientation):
    """Sets up the chess pieces on the board using pick and place."""
    frame_distance = 0.025
    origin_piece = 0.03125
    piece_position_map = {}
    piece_names = []
    spawned_piece_pose = deepcopy(board_pose)
    spawned_piece_pose.position.x += 0.3
    spawned_piece_pose.position.y += 0.05
    spawned_piece_pose.position.z += 0.02

    for row, line in enumerate(board_setup):
        rospy.loginfo("Iteration {}: ".format(row + 1))
        for col, piece in enumerate(line):
            if piece in pieces_xml:
                spawn_piece_position = deepcopy(spawned_piece_pose)
                model_name = "{}{}".format(piece, col)
                spawn_model(model_name, pieces_xml[piece], spawn_piece_position)
                piece_names.append(model_name)

                target_position = [
                    board_pose.position.x + frame_distance + origin_piece + row * (2 * origin_piece),
                    board_pose.position.y - 0.55 + frame_distance + origin_piece + col * (2 * origin_piece),
                    board_pose.position.z + 0.018 - 0.93
                ]  # Compensating for Gazebo-RViz origin difference

                piece_position_map["{}{}".format(row, col)] = target_position

                if piece != '*':  # Actual piece to be moved
                    pnp.pick(
                        Pose(
                            position=Point(x=spawn_piece_position.position.x, y=spawn_piece_position.position.y, z=target_position[2] - 0.015), 
                            orientation=overhead_orientation
                            )
                        )

                    pnp.place(
                        Pose(
                            position=Point(x=target_position[0], y=target_position[1], z=target_position[2] + 0.008), 
                            orientation=overhead_orientation
                            )
                        )

                    pnp.move_to_start(
                        Pose(
                            position=Point(x=0.7, y=0.135, z=0.35), 
                            orientation=overhead_orientation
                            )
                        )

    return piece_position_map, piece_names

def main():
    rospy.init_node("spawn_chessboard")
    rospy.wait_for_service("gazebo/spawn_sdf_model")

    pnp = PickAndPlaceMoveIt('left', 0.15)
    overhead_orientation = Quaternion(
        x=-0.0249590815779, y=0.999649402929, z=0.00737916180073, w=0.00486450832011
        )
    
    pnp.move_to_start(
        Pose(
            position=Point(x=0.7, y=0.135, z=0.35), 
            orientation=overhead_orientation
            )
        )

    # Table setup
    rospack = rospkg.RosPack()
    table_xml = load_model("{}/models/cafe_table/model.sdf".format(rospack.get_path('baxter_sim_examples')))
    table_pose = Pose(position=Point(x=0.73, y=0.4, z=0.0))
    spawn_model("cafe_table", table_xml, table_pose)

    # Chessboard setup
    rospack = rospkg.RosPack()
    board_pose = Pose(Point(0.3, 0.55, 0.78), Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0)))
    board_xml = load_model("{}/models/chessboard/model.sdf".format(rospack.get_path('baxter_chess')))
    spawn_model("chessboard", board_xml, board_pose)

    # Chess pieces setup
    pieces_xml = {
        piece: load_model("{}/models/{}.sdf".format(rospack.get_path('baxter_chess'), piece))
        for piece in 'rnbqkpRNBQKP'
    }
    board_setup = [
        'r******r', '', 'k*******', '', '', '*******K', '', 'R******R'
    ]
    piece_position_map, piece_names = set_up_chess_pieces(pnp, board_pose, pieces_xml, board_setup, overhead_orientation)




if __name__ == '__main__':
    sys.exit(main())