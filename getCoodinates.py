# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:58:57 2022
@author: 2540817538（有问题联系此QQ）
"""
import cv2
img = cv2.imread('/home/fusion/Documents/isualizer/img.png')
fw = open('/home/fusion/Documents/isualizer/coodinates.txt', 'a')


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print(x, y)
        fw.write(str(x)+' '+str(y))
        fw.write('\n')
        cv2.circle(img, (x, y), 2, (0, 0, 255))
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255))
        cv2.imshow("image", img)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
while (1):
    cv2.imshow("image", img)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
fw.close()
