'''import tkinter as tk'''
from PIL import Image
import numpy as np
import os
'''gui = tk.Tk() # initialize gui
gui.title("something")
gui.geometry("1080x720")'''


testNum = 0
while os.path.exists(f'D:\\github\\data sort test\\test{testNum}'):
    testNum += 1
def genDir(dir):
    path = dir[:dir.rfind("\\")]
    if not os.path.exists(path):
        os.makedirs(path)
    return(dir)
for slide in range(30):
    print(slide, end = "\r")
    for x in range(5):
        for y in range(3):
            for z in range(2):
                array = np.arange(0, 737280, 1, np.uint8) 
                array = np.reshape(array, (1024, 720)) 
                data = Image.fromarray(array) 
                data.save(genDir(f'D:\\github\\data sort test\\test{testNum}\\y{y}\\x{x}slide{slide}z{z}.png')) 