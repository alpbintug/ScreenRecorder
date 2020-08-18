import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics

SCREEN_SIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
FPS = 20.0
output = cv2.VideoWriter("output.avi",fourcc, FPS, (SCREEN_SIZE))
for i in range(200):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)

cv2.destroyAllWindows()
output.release()




