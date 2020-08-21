from cv2 import cv2
import numpy as np
import pyautogui
import tkinter as tk
import threading
import time
from PIL import Image
from mss import mss

cpdef bint keepRecording = False
frames = []

def _recordScreen():
    global frames,FPS, monitor
    timeForFrame = 1/FPS
    frames = []
    sct = mss()
    startTimer = time.time()
    currentTimer = time.time()
    while keepRecording == True:
        if(currentTimer-startTimer>1):
            print(len(frames))
            startTimer = currentTimer
        currentTimer = time.time()
        img = np.array(sct.grab(monitor))
        frames.append(img)
        
def recordScreen():
    threading.Thread(target=_recordScreen).start()
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
    global keepRecording, FPS
    btnStartRecording["state"] = "disabled"
    btnStopRecording["state"] = "normal"
    cpdef int X
    X = fpsSettings.current()
    FPS = float(X*5+10)
    print(FPS)
    window.iconify()
    keepRecording = True
    recordScreen()

def stopRecording():
    global keepRecording, FPS, SCREEN_SIZE
    keepRecording = False
    btnStartRecording["state"] = "normal"
    btnStopRecording["state"] = "disabled"
    saveVideo()
    
def saveVideo():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    print(SCREEN_SIZE)
    output = cv2.VideoWriter("output.avi",fourcc,FPS,(SCREEN_SIZE))
    converted = convertScreenShots(frames)
    outputVideo(output,converted)
    output.release()

cpdef float FPS = 0.0
SCREEN_SIZE = pyautogui.size()
monitor = {"top":0,"left":0,"width":SCREEN_SIZE[0],"height":SCREEN_SIZE[1]}
#outputVideo(output,converted)
cv2.destroyAllWindows()
#output.release()

window = tk.Tk()
window.geometry('300x300')
window.title("Screen Recorder")


labelFPSSetting = tk.Label(text = "Select FPS option")
labelFPSSetting.place(x=90, y=40)


fpsSettings = tk.ttk.Combobox(window)
fpsSettings['values'] = (10, 15, 20, 25, 30,35,40, 45,50,55, 60)
fpsSettings.current(4)
fpsSettings.place(x=90, y=80,width = 115)


btnStartRecording = tk.Button(window, text = "Start Recording",command = startRecording)
btnStartRecording.place(x=90, y=120)

btnStopRecording = tk.Button(window, text = "Stop Recording", command = stopRecording)
btnStopRecording.place(x=90,y=160)
btnStopRecording["state"] = "disabled"



window.mainloop()


