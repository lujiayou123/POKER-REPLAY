# !/user/bin/env Python3
# -*- coding:utf-8 -*-

"""
file：window.py.py
create time:2019/6/27 14:54
author:Loong Xu
desc: 窗口
"""
import tkinter as tk
from tkinter import filedialog, dialog
import os

window = tk.Tk()
window.title('窗口标题')  # 标题
window.geometry('500x500')  # 窗口尺寸

file_path = ''

file_text = ''

text1 = tk.Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()


def open_file():
    '''
    打开文件
    :return:
    '''
    global file_path
    global file_text
    file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
    print('打开文件：', file_path)
    if file_path is not None:
        with open(file=file_path, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
        text1.insert('insert', file_text)


bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
bt1.pack()

window.mainloop()  # 显示