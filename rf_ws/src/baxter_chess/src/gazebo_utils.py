import rospy
from gazebo_msgs.srv import SpawnModel

def load_model(model_path):
    """Reads and returns model XML from file."""
    with open(model_path, "r") as file:
        return file.read().replace("\n", "")


def spawn_model(model_name, model_xml, model_pose):
    """Spawns a model in Gazebo and handles errors."""
    try:
        spawn_service = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        spawn_service(model_name, model_xml, "/", model_pose, "world")
        rospy.loginfo("Spawned model '{}' successfully.".format(model_name))
    except rospy.ServiceException as e:
        rospy.logerr("Spawn SDF service call failed: {}".format(e))