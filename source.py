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

if __name__ == "__main__":
    FPS = 0.0
    SCREEN_SIZE = pyautogui.size()
    keepRecording = False
    frame = np.zeros(SCREEN_SIZE)
    monitor = {"top":0,"left":0,"width":SCREEN_SIZE[0],"height":SCREEN_SIZE[1]}
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    cv2.destroyAllWindows()

    window = tk.Tk()
    window.geometry('300x300')
    window.title("Screen Recorder")


    labelFPSSetting = tk.Label(text = "Select FPS option")
    labelFPSSetting.place(x=90, y=40)


    fpsSettings = tk.ttk.Combobox(window)
    fpsSettings['values'] = (10, 15, 20, 25, 30,35,40, 45,50,55, 60)
    fpsSettings.current(4)
    fpsSettings.place(x=90, y=80,width = 115)


    btnStartRecording = tk.Button(window, text = "Start Recording")
    btnStartRecording.place(x=90, y=120)

    btnStopRecording = tk.Button(window, text = "Stop Recording")
    btnStopRecording.place(x=90,y=160)
    btnStopRecording["state"] = "disabled"



    window.mainloop()


