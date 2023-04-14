#!/usr/bin/env python
# coding:utf-8

import rospy
import numpy as np
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import cv2
from .plot import *


def CompressedImgcallback(data):
    global bridge
    cv_img = bridge.compressed_imgmsg_to_cv2(data)
    cv2.imshow("frame", cv_img)
    cv2.waitKey(1)


def Imucallback(data):
    print(data.orientation_covariance)


def globalMapcallback(data):
    global bridge
    cv_img = bridge.imgmsg_to_cv2(data)
    cv2.imshow("frame", cv_img)
    cv2.waitKey(1)


def posecallback(pose):
    plot(pose)
    displaySpeed(pose)


def visualizerSub():
    # rospy.Subscriber('/camera/image_raw/compressed',
    #                  CompressedImage, CompressedImgcallback)
    # rospy.Subscriber('/imu_raw', Imu, Imucallback)
    rospy.Subscriber('/global_map', Image, globalMapcallback)
    rospy.Subscriber('/pose', String, posecallback)
