import cv2
import numpy as np


img = cv2.imread('/Users/guo/Desktop/digit_recognition/code/16-01/3.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 10
maxLineGap = 1
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(gray,(x1,y1),(x2,y2),255,2)

cv2.imshow('image', gray)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()