import rospy
from visualization_msgs.msg import Marker

"""
re-publish Marker message but in a different frame.
"""
def cb(msg):
    msg.header.frame_id = "osc/LARM_SCAPULA_LINK"
    pub.publish(msg)

rospy.init_node("tmp")
rospy.Subscriber("/predefined_trajectory_visualization", Marker, callback=cb)
pub = rospy.Publisher("/predefined_trajectory_visualization_rel", Marker, queue_size=10)
rospy.spin()