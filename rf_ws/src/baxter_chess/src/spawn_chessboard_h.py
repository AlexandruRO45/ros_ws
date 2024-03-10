#!/usr/bin/env python
import sys, rospy, tf, rospkg
from geometry_msgs.msg import Pose, Point, Quaternion
from pick_and_place_moveit import PickAndPlaceMoveIt
from utils import load_model, spawn_model  # Assuming utils.py contains load_model and spawn_model functions

def initialize_node():
    rospy.init_node("spawn_chessboard")
    rospy.wait_for_service("gazebo/spawn_sdf_model")

def move_baxter_to_start(pnp, overhead_orientation):
    pnp.move_to_start(Pose(position=Point(x=0.7, y=0.135, z=0.35), orientation=overhead_orientation))


def spawn_table(model_path):
    table_xml = load_model(model_path + "cafe_table/model.sdf")
    table_pose = Pose(position=Point(x=0.73, y=0.4, z=0.0))
    spawn_model("cafe_table", table_xml, table_pose)


def spawn_chessboard(model_path):
    orient = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
    board_pose = Pose(Point(0.3, 0.55, 0.78), orient)
    board_xml = load_model(model_path + "chessboard/model.sdf")
    spawn_model("chessboard", board_xml, board_pose)
    return board_pose


def setup_chess_pieces(model_path, board_pose, pnp, overhead_orientation):
    frame_dist = 0.025
    origin_piece = 0.03125
    pieces_xml, piece_positionmap, piece_names = {}, {}, []
    list_pieces = 'rnbqkpRNBQKP'
    board_setup = ['r******r', '', '**k*****', '', '', '******K*', '', 'R******R']
    
    for each in list_pieces:
        pieces_xml[each] = load_model(model_path + each + ".sdf")
    
    spawned_piece_pose = deepcopy(board_pose)
    spawned_piece_pose.position.x = 0.6
    spawned_piece_pose.position.y = 0.6
    spawned_piece_pose.position.z = 0.8

    for row, each_row in enumerate(board_setup):
        for col, piece in enumerate(each_row):
            pose = deepcopy(board_pose)
            pose.position.x += frame_dist + origin_piece + row * (2 * origin_piece)
            pose.position.y -= 0.55 + frame_dist + origin_piece + col * (2 * origin_piece)
            pose.position.z += 0.018
            piece_positionmap[str(row)+str(col)] = [pose.position.x, pose.position.y, pose.position.z-0.93] # Compensating Gazebo RViz origin difference
            
            if piece in pieces_xml:
                piece_name = "{}{}".format(piece, col)
                spawn_model(piece_name, pieces_xml[piece], spawned_piece_pose)

                 if piece in list_pieces:
                    piece_names.append(piece_name)
                    pick_pose = Pose(position=Point(x=spawned_piece_pose.position.x, y=spawned_piece_pose.position.y, z=piece_positionmap[str(row)+str(col)][2] - 0.015), orientation=overhead_orientation)
                    place_position = piece_positionmap[str(row)+str(col)]
                    place_pose = Pose(position=Point(x=place_position[0], y=place_position[1], z=place_position[2] + 0.008), orientation=overhead_orientation)
                    pnp.pick(pick_pose)
                    pnp.place(place_pose)
                    pnp.move_to_start(Pose(position=Point(x=0.7, y=0.135, z=0.35), orientation=overhead_orientation))

    return board_setup, list_pieces, piece_positionmap, piece_names, pieces_xml

def publish_ros_parameters(board_setup, list_pieces, piece_positionmap, piece_names, pieces_xml):
    rospy.set_param('board_setup', board_setup)
    rospy.set_param('list_pieces', list_pieces)
    rospy.set_param('piece_target_position_map', piece_positionmap)
    rospy.set_param('piece_names', piece_names)
    rospy.set_param('pieces_xml', pieces_xml)


def main():
    initialize_node()
    pnp = PickAndPlaceMoveIt('left', 0.15)
    overhead_orientation = Quaternion(x=-0.0249590815779, y=0.999649402929, z=0.00737916180073, w=0.00486450832011)

    move_baxter_to_start(pnp, overhead_orientation)

    model_path = rospkg.RosPack().get_path('baxter_sim_examples') + "/models/"
    spawn_table(model_path)

    model_path = rospkg.RosPack().get_path('baxter_chess') + "/models/"
    board_pose = spawn_chessboard(model_path)

    board_setup, list_pieces, piece_positionmap, piece_names, pieces_xml = setup_chess_pieces(model_path, board_pose, pnp, overhead_orientation)

    publish_ros_parameters(board_setup, list_pieces, piece_positionmap, piece_names, pieces_xml)

if __name__ == '__main__':
    main()