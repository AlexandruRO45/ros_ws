#!/usr/bin/env python
import sys, rospy, tf, rospkg
from gazebo_msgs.srv import *
from geometry_msgs.msg import *
from copy import deepcopy

# http://wiki.ros.org/simulator_gazebo/Tutorials/ListOfMaterials

class ChessboardDeleter:
  def __init__(self, list_pieces, board_setup):
    self.list_pieces = list_pieces
    self.board_setup = board_setup
    self.delete_model = None  # Initialize later

  def connect_to_gazebo(self):
    rospy.init_node("delete_chessboard")
    rospy.wait_for_service("gazebo/delete_model")
    self.delete_model = rospy.ServiceProxy("gazebo/delete_model", DeleteModel)

  def delete_pieces(self):
    for row, each in enumerate(self.board_setup):
      for col, piece in enumerate(each):
        if piece in self.list_pieces:
          piece_name = f"{piece}{col}"  # Use f-string for cleaner string formatting
          print(f"Deleting {piece_name}")
          self.delete_model(piece_name)

  def delete_cafe_table(self):
    print(f"Deleting cafe_table")
    self.delete_model("cafe_table")

  def delete_chessboard(self):
    print(f"Deleting chessboard")
    self.delete_model("chessboard")

if __name__ == '__main__':
  list_pieces = rospy.get_param('list_pieces')
  board_setup = rospy.get_param('board_setup')
  deleter = ChessboardDeleter(list_pieces, board_setup)
  deleter.connect_to_gazebo()
  deleter.delete_pieces()
  deleter.delete_cafe_table()
  deleter.delete_chessboard()


