#!/usr/bin/env python
#http://wiki.ros.org/simulator_gazebo/Tutorials/ListOfMaterials
import sys, rospy, tf, rospkg
from gazebo_msgs.srv import *
from geometry_msgs.msg import *
from copy import deepcopy
from pick_and_place_moveit import PickAndPlaceMoveIt


def model_load(model_path):
    with open(model_path, "r") as f:
        return f.read().replace("\n", "")

def model_spawn(model_name, model_xml, model_pose):
    try:
        spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        spawn_sdf(model_name, model_xml, "/", model_pose, "world")
        rospy.loginfo("Spawned model '{}' successfully.".format(model_name))
    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

def main():
    rospy.init_node("spawn_chessboard")
    rospy.wait_for_service("gazebo/spawn_sdf_model")
    
    # Baxter Start Position
    pnp = PickAndPlaceMoveIt('left', 0.15)
    overhead_orientation = Quaternion(x=-0.0249590815779, y=0.999649402929, z=0.00737916180073, w=0.00486450832011)
    pnp.move_to_start(Pose(position=Point(x=0.7, y=0.135, z=0.35), orientation=overhead_orientation))

    # Table
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/"
    table_xml = model_load(model_path + "cafe_table/model.sdf")
    table_pose = Pose(position=Point(x=0.73, y=0.4, z=0.0))
    model_spawn("cafe_table",table_xml,table_pose)

    # ChessBoard
    orient = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
    board_pose = Pose(Point(0.3,0.55,0.78), orient)
    frame_dist = 0.025
    model_path = rospkg.RosPack().get_path('baxter_chess')+"/models/"
    board_xml = model_load(model_path + "chessboard/model.sdf")
    model_spawn("chessboard", board_xml, board_pose)

    # Add chesspieces into the simulation
    origin_piece = 0.03125
    
    pieces_xml = dict()
    list_pieces = 'rnbqkpRNBQKP'
    for each in list_pieces:
        pieces_xml[each] = model_load(model_path + each + ".sdf")

    # Board setup (Standard chess game)
    #board_setup = ['rnbqkbnr', 'pppppppp', '', '', '', '', 'PPPPPPPP', 'RNBQKBNR']
    
    # Board setup (Simplified chess game)
    #board_setup = ['r******r', '', '**k*****', '', '', '******K*', '', 'R******R']
    board_setup = ['r******r', '', 'k*******', '', '', '*******K', '', 'R******R']

    piece_positionmap = dict()
    piece_names = []

    # hard coded position at the side of the chess board for spawning chess pieces
    spawned_piece_pose = deepcopy(board_pose)
    spawned_piece_pose.position.x = 0.6
    spawned_piece_pose.position.y = 0.6
    spawned_piece_pose.position.z = 0.8

    for row, each in enumerate(board_setup):
        rospy.loginfo("Iteration {}: ".format(row+1))
        for col, piece in enumerate(each):
            rospy.loginfo("Piece at position ({}, {}): {}".format(row, col, piece))
            
            pose = deepcopy(board_pose)
            pose.position.x = board_pose.position.x + frame_dist + origin_piece + row * (2 * origin_piece)
            pose.position.y = board_pose.position.y - 0.55 + frame_dist + origin_piece + col * (2 * origin_piece)
            pose.position.z += 0.018
            
            piece_positionmap[str(row)+str(col)] = [pose.position.x, pose.position.y, pose.position.z-0.93] #0.93 to compensate Gazebo RViz origin difference
            place_position = piece_positionmap[str(row)+str(col)]
            
            if piece in pieces_xml:
                model_spawn("%s%d" % (piece,col), pieces_xml[piece], spawned_piece_pose)
            
            if piece in list_pieces:
                piece_names.append("%s%d" % (piece,col))
                pnp.pick(Pose(position = Point(spawned_piece_pose.position.x,spawned_piece_pose.position.y,place_position[2] - 0.015), orientation = overhead_orientation))
                rospy.loginfo("Picking up piece: {}".format(piece))
                pnp.place(Pose(position = Point(place_position[0], place_position[1], place_position[2] + 0.008), orientation = overhead_orientation))
                rospy.loginfo("Placing piece at ({}, {}, {})".format(place_position[0],place_position[1],place_position[2]))
                pnp.move_to_start(Pose(position = Point(x=0.7, y=0.135, z=0.35), orientation=overhead_orientation))
            
            elif not piece == '*':
                rospy.loginfo('Error: No piece in this position: %s' % (piece))

    # Publish parameters to the ROS parameter server
    rospy.set_param('board_setup', board_setup) # Board setup
    rospy.set_param('list_pieces', list_pieces) # List of unique pieces
    rospy.set_param('piece_target_position_map', piece_positionmap) # 3D positions for each square in the chessboard
    rospy.set_param('piece_names', piece_names) # Pieces that will be part of the game
    rospy.set_param('pieces_xml', pieces_xml) # File paths to Gazebo models, i.e. SDF files


if __name__ == '__main__':
    sys.exit(main())