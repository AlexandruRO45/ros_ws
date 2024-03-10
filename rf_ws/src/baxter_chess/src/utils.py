import rospy
from gazebo_msgs.srv import SpawnModel


def load_model(model_path):
    with open(model_path, "r") as f:
        return f.read().replace("\n", "")

def spawn_model(model_name, model_xml, model_pose):
    try:
        spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        spawn_sdf(model_name, model_xml, "/", model_pose, "world")
    except rospy.ServiceException as e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))