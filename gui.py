import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import filedialog, dialog

def Load_Hand():
    print("Loading Hand")

# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('POKER REPLAY')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1920x1080')  # 这里的乘是小x
# 第4步，增加背景图片
photo = tk.PhotoImage(file="asserts/background.png")
theLabel = tk.Label(window,justify = tk.CENTER,image = photo,compound = tk.CENTER,font = ("华文行楷", 20),fg = "white")  # 前景色
theLabel.pack()
# # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
# menubar = tk.Menu(window)
# # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
# filemenu = tk.Menu(menubar, tearoff=0)
# # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_cascade(label="Load",command=Load_Hand)#加载手牌
# #创建菜单栏完成后，配置让菜单栏menubar显示出来
# window.config(menu=menubar)
text1 = tk.Text(window, width=150, height=100, bg='orange', font=('Arial', 12))
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


tk.mainloop()