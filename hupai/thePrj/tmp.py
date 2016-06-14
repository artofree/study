import cv2
from PIL import ImageGrab ,Image
import numpy as np
import pyautogui

print(pyautogui.size())


cv2.imshow('image', img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()