import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import gui_v1

def click_success():#触发函数
    print("success")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui_v1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click_success)#给id为pushButton的按钮添加触发
    sys.exit(app.exec_())