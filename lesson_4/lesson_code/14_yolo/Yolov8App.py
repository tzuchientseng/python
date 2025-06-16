#打開除錯功能 : Run/Edit Configuration/Emulate Terminal in output console 打勾
#pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio===2.0.2+cu118 -f https://download.pytorch.org/whl/cu118/torch_stable.html --no-cache-dir
#pip install pip install ultralytics
#pip install pyqt5
#qtdesigner
#將 .ui 檔轉換成 .py 檔 : File/settings/Tools/External Tools/+
#請參照 : http://mahaljsp.asuscomm.com/pycharm_qtdesigner/
#name : pyuic
#program : E:\yolov8_qt\venv\Scripts\pyuic5.exe
#Argument: $FileName$ -o $FileNameWithoutExtension$.py
#Working Directory : $ProjectFileDir$\ui
#然後在.ui檔按右鍵/External Tools/pyuic
import sys
import time

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidgetItem, QFileDialog

from DetectThread import DetectThread
from LoadModelThread import LoadModelThread
from PictureThread import PictureThread
from ui.ui_mainwindow import Ui_MainWindow
class Yolov8App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnPath.clicked.connect(self.btnPath_click)
        self.lblPath.setText("D:/pictures/primitive/2020/20200126_Philippines_day5_Boracay")
        self.path=self.lblPath.text()
        self.lblStatus.setText("載入模型中, 請稍後...")

        # 請一個新員工
        self.loadModelThread=LoadModelThread()
        # 約定打電話回來時，要執行什麼事
        self.loadModelThread.callback.connect(self.loadModelThreadCallback)
        # 命令員工開始工作
        self.loadModelThread.start()
    def loadModelThreadCallback(self, model):
        self.model=model
        self.lblStatus.setText("")
        self.pictureThread=PictureThread(self.path)
        self.pictureThread.callback.connect(self.pictureThreadCallback)
        self.pictureThread.start()
    def pictureThreadCallback(self, pix):
        btn=QPushButton()
        btn.setIcon(QIcon(pix))
        btn.setIconSize(QSize(400,300))
        btn.tag=pix.tag#圖檔絕對路徑
        btn.clicked.connect(self.btn_click)
        item=QListWidgetItem()
        item.setSizeHint(QSize(400,300))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, btn)
    def btn_click(self):
        btn=self.sender()
        self.lblStatus.setText('yolov8 辨識中....')
        self.t1=time.time()
        self.detectThread=DetectThread(self.model, btn.tag)
        self.detectThread.callback.connect(self.detectThreadCallback)
        self.detectThread.start()
    def detectThreadCallback(self, img):
        self.t2=time.time()
        self.lblStatus.setText(f'偵測時間 : {self.t2-self.t1:.7f}秒')
        pix=QPixmap(
            QImage(img,
                   img.shape[1],
                   img.shape[0],
                   img.shape[1]*3,
                   QImage.Format_RGB888
                   )
        )
        w=pix.width()
        h=pix.height()
        r=w/h
        label_width=self.lblImg.width()
        label_height=self.lblImg.height()
        label_r=label_width/label_height
        if r>label_r:
            pix=pix.scaled(label_width, label_width/r)
        else:
            pix=pix.scaled(label_height *r, label_height)
        self.lblImg.setPixmap(pix)
    def btnPath_click(self):
        self.path=QFileDialog.getExistingDirectory()
        if self.path!='':
            self.path=self.path.replace("\\","/")
            self.lblPath.setText(self.path)
            self.listWidget.clear()
            self.pictureThread=PictureThread(self.path)
            self.pictureThread.callback.connect(self.pictureThreadCallback)
            self.pictureThread.start()
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=Yolov8App()
    mainWindow.showMaximized()
    app.exec()