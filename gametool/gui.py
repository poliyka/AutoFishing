import tkinter as tk
from tkinter import StringVar, ttk
import touch
import threading
import csv

btn_start = ''

class App_start:
    def __init__(self,f1):
        self.f1=f1

        self.button()
        self.label()
        self.pack_place()
    
    def label(self):
        self.lb = tk.Label(self.f1,
                              text='熱鍵:\nF1:開始\nF2中斷\nESC:結束',
                              font=('標楷體', 12),
                              width=15,
                              height=5,
                              bg='Pink'
                              )
    def button(self):
        global btn_start
        btn_start = ttk.Button(self.f1,
                                  text='Start',
                                  width=10,
                                  cursor='hand2',
                                  command=self.btn_Start_click
                                  )
        # self.btn_delete = ttk.Button(self.f1,
        #                           text='Delete',
        #                           width=10,
        #                           cursor='hand2',
        #                           command=self.btn_delete_click
        #                           )
    # def btn_delete_click(self):
    #     with open('ouc.csv','r',newline='') as f:
    #         reader = csv.reader(f)
    #         rows = list(reader)
    #         rows = rows[:-1]
    #     with open('ouc.csv','w+',newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(rows)
            
    
    def btn_Start_click(self):
        t=threading.Thread(target=touch.start_listen)
        t.start()
        btn_start.config(state='disable')
    
    def pack_place(self):
        self.lb.pack()
        btn_start.pack()
        # self.btn_delete.pack()
        
def closeWindow():
    import os
    win.destroy()
    os._exit(0)


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('200x130+100+100')
    win.title('古劍自動釣魚程式')
    win.attributes("-topmost", 1) 
    f1 = tk.Frame(win)
    f1.pack()
    
    App_start(f1)
    touch.send_btn_start(btn_start)
    win.protocol('WM_DELETE_WINDOW', closeWindow)
    win.mainloop()