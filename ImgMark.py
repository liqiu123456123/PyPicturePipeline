import os
import os.path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QFontDialog,QMainWindow
from PyQt5.QtGui import QFontMetrics,QFontInfo
from PIL import Image, ImageDraw, ImageFont,ImageEnhance

class Ui_MarkWindow(QMainWindow):
    def __init__(self):
        super(Ui_MarkWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self) #

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 141, 391))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 30, 670, 151))
        self.groupBox.setObjectName("groupBox")

        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.radioButton.setChecked(True)# 默认选中
        self.radioButton.setObjectName("radioButton")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 74, 16))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 241, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.radioButton_2.setChecked(False)# 默认不选中
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 110, 95, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 74, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 110, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 190, 670, 71))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(270, 31, 64, 21))
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(340, 30, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('左上角')
        self.comboBox.addItem('右上角')
        self.comboBox.addItem('左下角')
        self.comboBox.addItem('右下角')
        self.comboBox.addItem('居中位置')
        self.comboBox.setCurrentIndex(0)

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.label_4.setObjectName("label_4")

        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 30, 181, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(150, 270, 670, 71))
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_6.setObjectName("label_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 30, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 350, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage('加载成功…… ')
        MainWindow.setStatusBar(self.statusBar)
        self.setStyleSheet("background-color: #E1FFFF;font-weight: bold;font-size: 14px;font-family: 'Microsoft YaHei';")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量添加水印"))
        self.pushButton.setText(_translate("MainWindow", "加载图片"))
        self.groupBox.setTitle(_translate("MainWindow", "水印设置"))
        self.radioButton.setText(_translate("MainWindow", "添加文字水印"))
        self.label.setText(_translate("MainWindow", "水印文字："))
        self.pushButton_2.setText(_translate("MainWindow", "字体设置"))
        self.radioButton_2.setText(_translate("MainWindow", "添加图片水印"))
        self.pushButton_3.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "水印图片："))
        self.groupBox_2.setTitle(_translate("MainWindow", "透明度及位置设置"))
        self.label_3.setText(_translate("MainWindow", "水印位置："))
        self.label_4.setText(_translate("MainWindow", "透明度："))
        self.groupBox_3.setTitle(_translate("MainWindow", "路径设置"))
        self.label_6.setText(_translate("MainWindow", "保存位置："))
        self.pushButton_4.setText(_translate("MainWindow", "浏览"))
        self.pushButton_5.setText(_translate("MainWindow", "执行"))
        self.pushButton.clicked.connect(self.getFiles)
        self.pushButton_2.clicked.connect(self.setFont)
        self.pushButton_3.clicked.connect(self.setImg)
        self.pushButton_4.clicked.connect(self.msg)
        self.pushButton_5.clicked.connect(self.addMark)
        self.listWidget.itemClicked.connect(self.itemClick)

    def setFont(self):
        self.waterfont, ok = QFontDialog.getFont()
        if ok:
            self.lineEdit.setFont(self.waterfont)
            self.fontSize = QFontMetrics(self.waterfont)
            self.fontInfo = QFontInfo(self.waterfont)

    def isImg(self,file):
        file = file.lower()
        if file == '.jpg':
            return True
        elif file == '.png':
            return True
        elif file == '.jpeg':
            return True
        elif file == '.bmp':
            return True
        else:
            return False

    def getFiles(self):
        try:
            self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
            self.list = os.listdir(self.img_path)
            num=0
            self.listWidget.clear()
            for i in range(0, len(self.list)):
                filepath = os.path.join(self.img_path, self.list[i])
                if os.path.isfile(filepath):
                    imgType = os.path.splitext(filepath)[1]
                    if self.isImg(imgType):
                        num += 1 #
                        self.item = QtWidgets.QListWidgetItem(self.listWidget)
                        self.item.setText(self.list[i])
            self.statusBar.showMessage('共有图片 '+str(num)+' 张')
        except Exception:
            QMessageBox.warning(None, '警告', '请选择一个有效路径……', QMessageBox.Ok)

    def itemClick(self, item):
        os.startfile(self.img_path + '\\' + item.text())

    def setImg(self):
        try:
            self.waterimg = QFileDialog.getOpenFileName(None,'选择水印图片','C:\\',"图片文件(*.jpeg;*.png;*.jpg;*.bmp)")
            self.lineEdit_2.setText(self.waterimg[0])
        except Exception as e:
            print(e)

    def msg(self):
        try:
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            self.lineEdit_3.setText(self.dir_path)
        except Exception as e:
            print(e)

    def textMark(self,img,newImgPath):
        im = Image.open(img).convert('RGBA')
        newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))
        font = ImageFont.truetype('simkai.ttf', self.fontInfo.pointSize())
        imagedraw = ImageDraw.Draw(newImg)
        imgwidth, imgheight = im.size
        txtwidth = self.fontSize.maxWidth() * len(self.lineEdit.text())
        txtheight = self.fontSize.height()


        if self.comboBox.currentText() == '左上角':
            position=(0,0)
        elif  self.comboBox.currentText() == '左下角':
            position=(0,imgheight - txtheight)
        elif  self.comboBox.currentText() == '右上角':
            position=(imgwidth - txtwidth,0)
        elif  self.comboBox.currentText() == '右下角':
            position=(imgwidth - txtwidth, imgheight - txtheight)
        elif  self.comboBox.currentText() == '居中位置':
            position=(imgwidth/2,imgheight/2)

        imagedraw.text(position, self.lineEdit.text(), font=font, fill="#FCA454")

        alpha = newImg.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(int(self.horizontalSlider.value())/10.0)
        newImg.putalpha(alpha)
        Image.alpha_composite(im, newImg).save(newImgPath)


    def imgMark(self,img,newImgPath):
        im = Image.open(img)
        mark = Image.open(self.lineEdit_2.text())
        rgbaim = im.convert('RGBA')
        rgbamark = mark.convert('RGBA')
        imgwidth, imgheight = rgbaim.size
        nimgwidth, nimgheight = rgbamark.size

        scale = 10
        markscale = max(imgwidth / (scale * nimgwidth), imgheight / (scale * nimgheight))
        newsize = (int(nimgwidth * markscale), int(nimgheight * markscale))
        rgbamark = rgbamark.resize(newsize, resample=Image.ANTIALIAS)
        nimgwidth, nimgheight = rgbamark.size
        if self.comboBox.currentText() == '左上角':
            position=(0,0)
        elif  self.comboBox.currentText() == '左下角':
            position=(0,imgheight - nimgheight)
        elif  self.comboBox.currentText() == '右上角':
            position=(imgwidth - nimgwidth,0)
        elif  self.comboBox.currentText() == '右下角':
            position=(imgwidth - nimgwidth, imgheight - nimgheight)
        elif  self.comboBox.currentText() == '居中位置':
            position=(int(imgwidth/2),int(imgheight/2))
        rgbamarkpha = rgbamark.convert("L").point(lambda x: x/int(self.horizontalSlider.value()))
        rgbamark.putalpha(rgbamarkpha)
        rgbaim.paste(rgbamark, position, rgbamarkpha)
        try:
            rgbaim.save(newImgPath)
        except Exception:
            QMessageBox.warning(None, '错误', '请选择其他路径……', QMessageBox.Ok)

    def addMark(self):
        if self.lineEdit_3.text() == '':
            QMessageBox.warning(None,'警告','请选择保存路径',QMessageBox.Ok)
            return
        else:
            num = 0  # 记录处理图片数量
            for i in range(0, self.listWidget.count()): # 遍历图片列表
                # 设置原始图片路径（包括文件名）
                filepath = os.path.join(self.img_path, self.listWidget.item(i).text())
                # 设置水印图片保存路径（包括文件名）
                newfilepath = os.path.join(self.lineEdit_3.text(), self.listWidget.item(i).text())
                if self.radioButton.isChecked(): # 判断是否选择文字水印单选按钮
                    if self.lineEdit.text() == '': # 判断是否输入了水印文字
                        QMessageBox.warning(None, '警告', '请输入水印文字', QMessageBox.Ok)
                        return
                    else:
                        self.textMark(filepath,newfilepath) # 调用textMark方法添加文字水印
                        num += 1 # 处理图片数量加1
                else:
                    if self.lineEdit_2.text() != '': # 判断水印图片不为空
                        self.imgMark(filepath,newfilepath) # 调用imgMark方法添加图片水印
                        num += 1 # 处理图片数量加1
                    else:
                        QMessageBox.warning(None, '警告', '请选择水印图片', QMessageBox.Ok)
            self.statusBar.showMessage('任务完成，此次共处理 ' + str(num) + ' 张图片')  # 显示处理图片总数
