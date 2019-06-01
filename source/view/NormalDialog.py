# -*- coding:utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import os
from util import loadUiType
from util import DIR

UI_PATH = os.path.join(DIR,"ui","dialog.ui")

form_class , base_class = loadUiType(UI_PATH)

class NormalDialog(base_class,form_class):
    def __init__(self,parent):
        super(NormalDialog,self).__init__()
        self.parent_window = parent
        self.setupUi(self)
        # Note 不带窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.OK_BTN.clicked.connect(self.close)

    def display(self,title,msg):
        # Note 设置标题和输出信息
        self.Title_Label.setText(title)
        self.Message_Label.setText(msg)

        width = self.parent_window.size().width()
        height = self.parent_window.size().height()

        # Note 居中显示
        centerX = width/2 - self.geometry().width()/2
        centerY = height/2 - self.geometry().height()/2
        position = self.parent_window.mapToGlobal(QPoint(centerX,centerY))
        self.move(position)

        # Note 添加灰色遮盖
        self.label = QLabel(self.parent_window)
        self.label.resize(width, height)
        self.label.setStyleSheet('background:rbga(0, 0, 0, 125)')

        # Note 显示效果
        self.label.show()
        self.show()
    
    def close(self):
        self.label.close()
        return super(NormalDialog,self).close()