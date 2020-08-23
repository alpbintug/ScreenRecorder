from cv2 import cv2
import numpy as np
import pyautogui
import tkinter as tk
import threading
import time
from PIL import Image
from mss import mss
from numba import jit



from concurrent.futures import ThreadPoolExecutor
###################################################
#Yukardaki kütüphaneyle Numba'yı birleştirip bi şeyler yap
#Çok hızlı oluyomuş öyle diyolar
###################################################
#GLOBALLERİ KALDIR
#DÜZGÜN KOD YAZ KÖLE
###################################################
#frames = [] yazmak yerine = np.zeros(SCREEN_SIZE) gibi bi şeyler dene
#Numba'da bu daha hızlı oluyomuş
###################################################






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
    timeForFrame = 1/FPS
    img = np.zeros(SCREEN_SIZE)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("output.avi",fourcc,FPS,(SCREEN_SIZE))
    sct = mss()
    i = 0
    thread = threading.Thread(target=_recordScreen, args=[FPS,monitor,SCREEN_SIZE])
    thread.start()
    while keepRecording == True:
        _recordScreen(monitor, output, sct)
        i+=1
        if(i%30==0):
            print(time.time())
    
    output.release()
@jit
def _recordScreen(monitor,output,sct):
    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
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


