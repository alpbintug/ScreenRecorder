from cv2 import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
FPS = 20
videoLength = 10
output = cv2.VideoWriter("output.avi",fourcc, FPS, (SCREEN_SIZE))
for i in range(FPS*videoLength):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)

cv2.destroyAllWindows()
output.release()




