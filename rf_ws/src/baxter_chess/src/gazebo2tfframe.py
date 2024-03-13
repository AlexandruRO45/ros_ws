#!/usr/bin/env python
import rospy
import tf
from gazebo_msgs.msg import LinkStates

class Gazebo2TFFrame:
    def __init__(self, link_name):
        self.pose = {}
        self.input_linkname = link_name

        # Initialize ROS node
        rospy.init_node('gazebo2tfframe')

        # Create TF broadcaster -- this will publish a frame given a pose
        self.tfBroadcaster = tf.TransformBroadcaster()

        # Subscribe to Gazebo's topic where all links and objects poses within the simulation are published
        rospy.Subscriber('gazebo/link_states', LinkStates, self.get_links_gazebo)

    def get_links_gazebo(self, link_states_msg):
        # Callback to retrieve the object you are interested in
        poses = {'world': link_states_msg.pose[0]}  # get world link
        for (link_idx, link_name) in enumerate(link_states_msg.name):
            modelname = link_name.split('::')[0]
            if self.input_linkname == modelname:
                poses[modelname] = link_states_msg.pose[link_idx]

        self.pose = poses[self.input_linkname]

    def run(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            if self.pose is not None:
                pos = self.pose.position
                ori = self.pose.orientation
                rospy.loginfo(pos)
                # Publish transformation given in pose
                self.tfBroadcaster.sendTransform((pos.x, pos.y, pos.z - 0.93), (ori.x, ori.y, ori.z, ori.w),
                                                 rospy.Time.now(), self.input_linkname, 'world')
                rate.sleep()

def main():
    for name in rospy.get_param('piece_names'):
        gazebo_instance = Gazebo2TFFrame(name)
        gazebo_instance.run()

if __name__ == '__main__':
    main()
