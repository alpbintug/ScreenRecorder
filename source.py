from cv2 import cv2
import numpy as np
import pyautogui
import tkinter as tk
import threading
import time
from PIL import Image
from mss import mss
from numba import jit
from multiprocessing import Queue, Process

def stopRecording():
    global keepRecording, btnStartRecording,btnStopRecording
    keepRecording = False
    btnStartRecording["state"] = "normal"
    btnStopRecording["state"] = "disabled"

def startRecording(monitor,SCREEN_SIZE):
    global keepRecording, btnStartRecording,btnStopRecording
    btnStartRecording["state"] = "disabled"
    btnStopRecording["state"] = "normal"
    keepRecording = True
    X = fpsSettings.current()
    FPS = float(X*5+10)
    print(FPS)
    window.iconify()
    #_recordScreen(FPS,monitor,keepRecording,SCREEN_SIZE)
    threading.Thread(target=recordScreen,args=[FPS,monitor,SCREEN_SIZE]).start()
def recordScreen(FPS,monitor,SCREEN_SIZE):
    global keepRecording
    #timeForFrame = 1/FPS
    #img = np.zeros(SCREEN_SIZE)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("output.avi",fourcc,FPS,(SCREEN_SIZE))
    sct = mss()
    queue = Queue()
    threading.Thread(target=_recordScreen,args=[monitor,sct,queue]).start()
    threading.Thread(target=_writeScreen,args=[output,queue]).start()
    output.release()

def _recordScreen(monitor,sct,queue):
    i = 0
    while keepRecording == True:
        queue.put(np.array(sct.grab(monitor)))
        i+=1
        if(i%30==0):
            print(time.time(), queue.qsize())
    queue.put(None)


def _writeScreen(output, queue):
    while keepRecording == True:
        img = queue.get()
        print(img)
        if img is None:
            break
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2RGB)
        output.write(img)


if __name__ == "__main__":
    keepRecording = False
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


    btnStartRecording = tk.Button(window, text = "Start Recording",command = lambda : startRecording(monitor,SCREEN_SIZE) )
    btnStartRecording.place(x=90, y=120)

    btnStopRecording = tk.Button(window, text = "Stop Recording", command = stopRecording)
    btnStopRecording.place(x=90,y=160)
    btnStopRecording["state"] = "disabled"



    window.mainloop()


