# -*- coding:utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


from data import common_chinese_list
from data import poem_data

from view.NormalDialog import NormalDialog

import os
import random
from functools import partial
from util import loadUiType
from util import DIR

UI_PATH = os.path.join(DIR,"ui","game.ui")

form_class , base_class = loadUiType(UI_PATH)

class GameView(base_class,form_class):
    def __init__(self):
        super(GameView,self).__init__()
        self.setupUi(self)

        self.score = 0
        self.question_char = ''
        self.message_box = NormalDialog(self)

        # Note 将按钮添加到数组当中
        self.answer_list = []
        self.answer_list.append(self.Answer_1)
        self.answer_list.append(self.Answer_2)
        self.answer_list.append(self.Answer_3)
        self.answer_list.append(self.Answer_4)
        self.answer_list.append(self.Answer_5)
        self.answer_list.append(self.Answer_6)
        self.answer_list.append(self.Answer_7)
        self.answer_list.append(self.Answer_8)
        
        # Note 循环数组添加点击事件
        for answer in self.answer_list:
            answer.clicked.connect(partial(self.checkAnswer,answer))

        self.poemDataHandler()
    
    def checkAnswer(self,button):
        if button.text() == self.question_char:
            self.message_box.display(u"回答正确", u"恭喜你回答正确")
            self.score += 1
            self.Score_Label.setText(u"学习积分: %s" % self.score)
            self.poemDataHandler()
        else:
            self.message_box.display(u"回答错误", u"请重新作答")
        
    def poemDataHandler(self):
        rand = random.randint(0,len(poem_data)-1)
        
        poem_info = poem_data[rand]

        body   = poem_info['body']
        name   = poem_info['name']
        author = poem_info['author']

        # Note 模仿 do while 语句截取字符
        while True:
            num = random.randint(0,len(body)-1)
            self.question_char = body[num]
            if self.question_char != '\n':
                break
        
        # Note 添加下划线标注
        body = body[0:num] + '__' + body[num+1:]
        poem = ""
        poem += "<p align=\"center\">%s</p>" % name
        poem += "<p align=\"center\">%s</p>" % author
        for line in body.split("\n"):
            poem += "<p align=\"center\">%s</p>" % line

        self.Poem_Label.setText(poem)
        
        # Note 循环数组添加点击事件
        for answer in self.answer_list:
            rand = random.randint(0,len(common_chinese_list)-1)
            answer.setText(common_chinese_list[rand])

        rand = random.randint(0,len(self.answer_list)-1)
        self.answer_list[rand].setText(self.question_char)
        