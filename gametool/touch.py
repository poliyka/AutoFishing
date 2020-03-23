import gui
import catchimage
import math_image
from StringPool import VK_CODE,VK_SHIFT_CODE

import win32gui
import win32ui
import win32con
import win32api
import csv
import time
import numpy as np
import threading
import tkinter as tk
from tkinter import StringVar, ttk
from pynput.keyboard import Controller, Key, Listener
from pynput import keyboard


hwnd = win32gui.FindWindow(None, '古劍奇譚網路版 [琴心劍魄 - 步雲區] 2.0.1.13082')

# -----自動發話系統------
def press(*args, sleep=0):
    """
    順序按下釋放按鍵
    :param hwd:
    :param args:
    :return:
    """
    for arg in args:
        if arg in VK_SHIFT_CODE:
            press_hold_release("left_shift", VK_SHIFT_CODE[arg])
        else:
            win32api.keybd_event(VK_CODE[arg],0, 0, 0)
            time.sleep(.05)
            win32api.keybd_event(VK_CODE[arg],0, win32con.KEYEVENTF_KEYUP,  0)
    if sleep > 0:
        time.sleep(sleep)

def press_hold_release(*args):
    """
    組合建按下與釋放
    :param args:
    :return:
    """
    for arg in args:
        win32api.keybd_event(VK_CODE[arg], 0, 0, 0)
        time.sleep(.05)

    for arg in args:
        win32api.keybd_event(VK_CODE[arg], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.05)


def set_font(text):
    for i in list(text):

        if i in VK_CODE:
            win32api.keybd_event(VK_CODE[i], 0, 0, 0)
            win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            press(i)
            
        
    win32api.keybd_event(VK_CODE['enter'], 0, 0, 0)
    win32api.keybd_event(VK_CODE['enter'], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE['enter'], 0, 0, 0)
    win32api.keybd_event(VK_CODE['enter'], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE['enter'], 0, 0, 0)
    win32api.keybd_event(VK_CODE['enter'], 0, win32con.KEYEVENTF_KEYUP, 0)


# ----自動釣魚系統-----
ocu = []
count = 0
loop = 0
_exit = ''
percent = ''
angle = ''

def delay_time(t):
    global _exit
    delay = time.perf_counter() + t
    while time.perf_counter() < delay:
        if _exit != keyboard.Key.f2:
            pass
        else:
            _exit = keyboard.Key.f2
            break
    
def check_exit(key):
    # 加入程式中斷判斷
    if key == keyboard.Key.f2:
        global _exit
        _exit = keyboard.Key.f2
    else:
        t = threading.Thread(target=on_press,args=(key,))
        t.start()

def on_press(key):
    # if key == keyboard.Key.f12:
    #     set_font(r"I'm Iron men.?")
    #     time.sleep(1)
    #     set_font(r"ji3g4a/6vup ")
    #     time.sleep(1)
    #     set_font(r"fu/32ji 2ji 53rlu4")

    if key == keyboard.Key.f1:
    # if key == keyboard.KeyCode(VK_CODE['q']):
        # 司命職業任務用
        # while _exit !=keyboard.Key.f2:
        #     win32api.keybd_event(VK_CODE['q'], 0, 0, 0)
        #     win32api.keybd_event(VK_CODE['q'], 0, win32con.KEYEVENTF_KEYUP, 0)
        #     time.sleep(2)
            
        
        
        global _exit
        # while _exit != keyboard.Key.f2:
        if _exit != keyboard.Key.f2:
            global count
            global t
            global ocu
            global loop
            global percent,angle
            
            if count == 0 :
                win32api.keybd_event(VK_CODE['q'], 0, 0, 0)
                win32api.keybd_event(VK_CODE['q'], 0, win32con.KEYEVENTF_KEYUP, 0)
                delay_time(8.5)
                if _exit != keyboard.Key.f2:
                    catchimage.window_capture()
                    # 加入判斷延時
                    time_count = 0
                    while math_image.math_image_range() == False:
                        if _exit != keyboard.Key.f2:
                            catchimage.window_capture()
                            time_count+=1
                            print(time_count)
                            if time_count > 50:
                                break
                        else:
                            break
                        
                    try:
                        if _exit != keyboard.Key.f2:
                            math_image.math_image_range()
                            t = time.perf_counter()
                            
                            percent,angle = math_image.get_index()
                            
                            # 直接取角度與時間線性方程式
                            sec=0.10375+0.00327*angle
                            
                            print(sec)
                            delay_time(sec)
                            win32api.keybd_event(VK_CODE['q'], 0, 0, 0)
                            win32api.keybd_event(VK_CODE['q'], 0, win32con.KEYEVENTF_KEYUP, 0)
                            print(time.perf_counter() - t)
                            
                            # 重複釣魚(前後移動消除動作延遲)
                            # if loop == 0:
                            #     delay_time(3)
                            #     win32api.keybd_event(VK_CODE['a'], 0, 0, 0)
                            #     delay_time(0.5)
                            #     win32api.keybd_event(VK_CODE['a'], 0, win32con.KEYEVENTF_KEYUP, 0)
                            #     loop = 1
                            # else:
                            #     delay_time(3)
                            #     win32api.keybd_event(VK_CODE['d'], 0, 0, 0)
                            #     delay_time(0.5)
                            #     win32api.keybd_event(VK_CODE['d'], 0, win32con.KEYEVENTF_KEYUP, 0)
                            #     loop = 0
                                
                            # count += 1
                            # on_press(keyboard.Key.f1)
        
                    except:
                        print('操作延時')
                        # on_press(keyboard.Key.f1)
                # 收集數據用 
                # else:
                #     t_end = time.perf_counter() - t
                #     print(time.perf_counter() - t)
                    
                #     ocu = [float(percent),float(angle),t_end]
                #     with open('ouc.csv','a+',newline='') as f:
                #         writer = csv.writer(f)
                #         writer.writerow(ocu)
                    # np.savetxt('ouc.csv', ocu, fmt="%5.2f", delimiter=",")
                    
        #             # count = 0
        _exit = ''
btn_start = ''
def send_btn_start(btn):
    global btn_start
    btn_start = btn
    
def on_release(key):
    global btn_start
    if key == keyboard.Key.esc:
        btn_start.config(state='active')
        return False
    if key == keyboard.Key.f2:
        return False

def start_listen():
    global _exit 
    global count
    count = 0
    _exit = ''
    with Listener(on_press=check_exit, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    
    # 開始監聽,按esc退出監聽
    start_listen()
    
    
