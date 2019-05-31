# -*- coding:utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import util
import sys
import os

from view import TitleView
from view import GameView

class PoemMaster(QWidget):
    def __init__(self):
        super(PoemMaster,self).__init__()
        self.setWindowTitle(u"古诗词背诵软件")
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.initUI()
        
    def initUI(self):
        self.title_view = TitleView()
        self.title_view.Study_BTN.clicked.connect(self.viewNavigator)
        self.game_view = GameView()
        self.game_view.Back_Button.clicked.connect(self.viewNavigator)
        self.game_view.setVisible(False)

        self.layout().addWidget(self.title_view)
        self.layout().addWidget(self.game_view)

    def viewNavigator(self):
        self.title_view.setVisible(not self.title_view.isVisible())
        self.game_view.setVisible(not self.game_view.isVisible())
        self.adjustSize()

def main():
    app = QApplication([]) 
    window = PoemMaster()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    
    