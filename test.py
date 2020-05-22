#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('POKER REPLAY')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1920x1080')  # 这里的乘是小x

# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=210, width=140)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='./deck/As.png')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(960, 540, anchor='n', image=image_file)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
canvas.pack()

# 第7步，主窗口循环显示
window.mainloop()