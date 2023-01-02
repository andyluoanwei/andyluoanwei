import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QWidget, QAction, qApp, QStatusBar, QMenu, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   
        # self.push_button()
        self.setWindow_title()
        self.layout_UI()
        self.menu_bar()
        self.too_Bar()
        self.status_bar()


# QPushButton
    def push_button(self):
        # 窗口关闭控件...
        q_btn = QPushButton('Quit', self)
        q_btn.clicked.connect(QCoreApplication.instance().quit)
        q_btn.resize((q_btn.sizeHint()))
        q_btn.move(220, 30)

# 设置窗口标签、图标、位置及大小
    def setWindow_title(self):
        label_1 = QLabel("Zet_code", self)
        label_1.move(100, 100)

        label_2 = QLabel("Tutorials", self)
        label_2.move(135, 140)

        label_3 = QLabel("For Programming", self)
        label_3.move(165, 180)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Andy's Window_Design")
        self.setWindowIcon(QIcon('icon/icon.png'))
        self.statusBar()
        self.center()
        self.show()

# 窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# 消息盒子
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# 菜单栏
    def menu_bar(self):
        # 实例化menubar
        menubar = self.menuBar()
        # 一级菜单栏创建
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        selectMenu = menubar.addMenu('&Select')
        viewMenu = menubar.addMenu('&View')
        self.view(viewMenu)
        navigateMenu = menubar.addMenu('&Navigate')
        codeMenu = menubar.addMenu('&Code')
        refactorMenu = menubar.addMenu('&Refactor')
        runMenu = menubar.addMenu('&Run')
        toolsMenu = menubar.addMenu('&Tools')
        vcsMenu = menubar.addMenu('&VCS')
        windowMenu = menubar.addMenu('&Window')
        helpsMenu = menubar.addMenu('&Help')

        # 二级菜单
        # new
        new_Act = QAction(QIcon('icon/new.png'), '&New', self)
        new_Act.setShortcut('Ctrl+N')
        new_Act.setStatusTip('New application')

        # import
        imp_Menu = QMenu('Import', self)
        imp_Act = QAction('Import email', self)
        imp_Menu.addAction(imp_Act)

        # Exit
        exitAct = QAction(QIcon('icon/icon.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        fileMenu.addAction(new_Act)
        fileMenu.addMenu(imp_Menu)
        fileMenu.addAction(exitAct)

# 工具栏
    def too_Bar(self):
        exitAct = QAction(QIcon('icon/exit.png'), 'Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)


# 勾选菜单
    def view(self, viewMenu):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('ready')

        viewSttAct = QAction('View statusbar', self, checkable=True)
        viewSttAct.setStatusTip('View statusbar')
        viewSttAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewSttAct)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

# 右键菜单
    def contextMenuEvent(self, event):
        c_menu = QMenu(self)

        newAct = c_menu.addAction("New")
        opn_Act = c_menu.addAction("Open")
        quit_Act = c_menu.addAction("Quit")
        action = c_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_Act:
            qApp.quit()

# 布局管理
    def layout_UI(self):
        label_1 = QLabel("Zet_code", self)
        label_1.move(100, 100)

        label_2 = QLabel("Tutorials", self)
        label_2.move(135, 140)

        label_3 = QLabel("For Programming", self)
        label_3.move(155, 170)


# 状态栏
    def status_bar(self):
        self.statusBar().showMessage('Ready...')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
