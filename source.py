from cv2 import cv2
import numpy as np
import pyautogui

def recordScreen(FPS,Length):
    screenShots = []
    for i in range (FPS*Length):
        img = pyautogui.screenshot()
        screenShots.append(img)
    return screenShots

def convertScreenShots(screenShots):
    converted = []
    for i in range(len(screenShots)):
        frame = np.array(screenShots[i])
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        converted.append(frame)
    return converted

def outputVideo(output, screenShots):
    for i in range(len(screenShots)):
        output.write(screenShots[i])



SCREEN_SIZE = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
FPS = 20
videoLength = 1
output = cv2.VideoWriter("output.avi",fourcc, FPS, (SCREEN_SIZE))
recorded = recordScreen(FPS,videoLength)
converted = convertScreenShots(recorded)
outputVideo(output,converted)
cv2.destroyAllWindows()
output.release()




