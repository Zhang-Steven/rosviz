import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from std_msgs.msg import String
import rospy


def globalmapPub():
    global bridge
    bridge = CvBridge()
    pub = rospy.Publisher('/global_map', Image, queue_size=10)

    rospy.init_node('globalmapPub', anonymous=True)
    rate = rospy.Rate(10)
    globalImg = cv2.imread('/home/fusion/Documents/isualizer/img.png')
    # cv2.imshow('unprocessed', globalImg)
    # cv2.waitKey()
    while not rospy.is_shutdown():
        pub.publish(bridge.cv2_to_imgmsg(globalImg, encoding='bgr8'))
        rate.sleep()


def posePub():

    msg = rospy.Publisher('/pose', String, queue_size=10)
    rospy.init_node('posePub', anonymous=True)
    rate = rospy.Rate(10)
    f = open('/home/fusion/Documents/isualizer/pose.txt', 'r')
    while not rospy.is_shutdown():
        line = f.readline()
        if not line:
            break
        rospy.loginfo(line)
        msg.publish(line)
        rate.sleep()


def visualizerProcess():
    globalmapPub()
    posePub()
