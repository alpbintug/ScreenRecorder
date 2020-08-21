from cv2 import cv2
import numpy as np
import pyautogui
import tkinter as tk
import threading
import time
from PIL import Image
from mss import mss
from numba import jit

keepRecording = False
frames = []

        
def recordScreen():
    
    global frames,FPS, monitor
    frames = []
    threading.Thread(target=_recordScreen,args=[FPS]).start()
def _recordScreen(FPS):
    timeForFrame = 1/FPS
    sct = mss()
    startTimer = time.time()
    currentTimer = time.time()
    #t_getScreenShot = threading.Timer(timeForFrame,_getScreenShot,args=[sct])
    #t_getScreenShot.start()
    while keepRecording == True:
        threading.Thread(target=_getScreenShot,args=[sct]).start()
        if(currentTimer-startTimer>1):
            print(len(frames))
            startTimer = currentTimer
        currentTimer = time.time()
        #threading.Thread(target=_getScreenShot,args=[sct]).start()
    #t_getScreenShot.cancel()
def _getScreenShot(sct):
    global frames, monitor
    img = np.array(sct.grab(monitor))
    frames.append(img)
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
    global frames
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    print(SCREEN_SIZE)
    output = cv2.VideoWriter("output.avi",fourcc,FPS,(SCREEN_SIZE))
    converted = convertScreenShots(frames)
    frames = []
    outputVideo(output,converted)
    output.release()

FPS = 0.0
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


