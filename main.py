from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QBrush, QPixmap
import imageRename, imageMark  # 导入模块


class Ui_MainWindow(QtWidgets.QWidget):

    # 自动生成的代码，用来对窗体进行设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.actionMark = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/mark.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMark.setIcon(icon)
        self.actionMark.setObjectName("actionMark")
        self.actionRename = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/rename.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon1)
        self.actionRename.setObjectName("actionRename")
        self.menu.addAction(self.actionMark)
        self.menu.addAction(self.actionRename)
        self.menubar.addAction(self.menu.menuAction())
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_2.menuAction())
        palette = QtGui.QPalette()
        palette.setBrush(MainWindow.backgroundRole(), QBrush(
            QPixmap("img/back.png").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
                                           QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setFixedSize(800, 600);
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPicturePipeline"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "|| 关于"))
        self.actionMark.setText(_translate("MainWindow", "添加水印"))
        self.actionRename.setText(_translate("MainWindow", "批量重命名"))
        self.actionAbout.setText(_translate("MainWindow", "关于本软件"))
        # 关联“添加水印”菜单的方法
        self.actionMark.triggered.connect(self.openMark)
        # 关联“批量重命名”菜单的方法
        self.actionRename.triggered.connect(self.openRename)
        # 关联“关于本软件”菜单的方法
        self.actionAbout.triggered.connect(self.about)

    # 打开水印窗体
    def openMark(self):
        self.another = imageMark.Ui_MarkWindow()  # 创建水印窗体对象
        self.another.show()  # 显示窗体

    # 打开重命名窗体
    def openRename(self):
        self.another = imageRename.Ui_RenameWindow()  # 创建重命名窗体对象
        self.another.show()  # 显示窗体

    # 关于本软件
    def about(self):
        QMessageBox.information(None, '关于本软件',
                                'PyPicturePipeline是一款专为日常工作设计的工具软件，它极大地简化了为图片添加文字水印和图片水印的流程。使用这款软件，您可以轻松地自定义水印的位置和透明度，以满足不同需求。除此之外，它还提供了图片文件重命名的功能，支持将文件名转换为大写或小写，甚至允许您根据自定义模板对图片文件进行编号，从而更高效地管理和组织图片文件。',
                                QMessageBox.Ok)


# 主方法
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
