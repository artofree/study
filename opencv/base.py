__author__ = 'guo'
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('/Users/guo/Projects/study/unify/assets/photo/1.jpg', 0)

cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
