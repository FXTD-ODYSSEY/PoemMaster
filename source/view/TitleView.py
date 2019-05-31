# -*- coding:utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import os
from util import loadUiType
from util import DIR

UI_PATH = os.path.join(DIR,"ui","title.ui")

form_class , base_class = loadUiType(UI_PATH)

class TitleView(base_class,form_class):
    def __init__(self):
        super(TitleView,self).__init__()
        self.setupUi(self)
        
        