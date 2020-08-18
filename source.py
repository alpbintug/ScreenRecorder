from cv2 import cv2
import numpy as np
import pyautogui
import tkinter as tk

keepRecording = False;
frames = []

def recordScreen(FPS):
    screenShots = []
    while keepRecording == True:
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

def startRecording():
    FPS = fpsSettings.get();
    #window.iconify()
    keepRecording = True;
    #output = cv2.VideoWriter("output.avi",fourcc, FPS, (SCREEN_SIZE))
    frames = recordScreen(FPS)

SCREEN_SIZE = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
videoLength = 1
#converted = convertScreenShots(recorded)
#outputVideo(output,converted)
cv2.destroyAllWindows()
#output.release()

window = tk.Tk()
window.geometry('300x300')
window.title("Screen Recorder")


labelFPSSetting = tk.Label(text = "Select FPS option")
labelFPSSetting.place(x=90, y=40)


fpsSettings = tk.ttk.Combobox(window)
fpsSettings['values'] = (10, 15, 20, 25, 30, 45, 60)
fpsSettings.current(4)
fpsSettings.place(x=90, y=80,width = 115)


btnStartRecording = tk.Button(window, text = "Start Recording",command = startRecording)
btnStartRecording.place(x=90, y=120)

btnStopRecording = tk.Button(window, text = "Stop Recording")
btnStopRecording.place(x=90,y=160)
btnStopRecording["state"] = "disabled"



window.mainloop()


