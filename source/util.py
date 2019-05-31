#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import os
import json
DIR = os.path.dirname(__file__)


def loadUiType(uiFile=""):
    """
    loadUiType [读取UI文件]
    
    [description]
    根据python版本以及PyQt或者PySide的不同版本进行统一的ui文件读取
    生成原理：
    过去我们借助 uic 工具将Qt Designer生成的ui文件编译成Python文件进行调用
    这个函数就是将这个步骤放到了代码中执行，生成的结果将会直接运行到内存中
    
    兼容 Python3 & Python2

    Keyword Arguments:
        uiFile {str} -- ui文件的路径 (default: {""})
    
    Returns:
        base_class
    """
    import pyside2uic as uic
    import xml.etree.ElementTree as xml
    # Note 兼容Python3
    try:
        from cStringIO import StringIO
    except:
        from io import StringIO


    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    # Note 兼容Python3
    try:
        with open(uiFile, 'r') as f:
            o = StringIO()
            frame = {}
            
            uic.compileUi(f, o, indent=0)
            pyc = compile(o.getvalue(), '<string>', 'exec')
            exec (pyc) in frame

            form_class = frame['Ui_%s'%form_class]
            base_class = eval('%s'%widget_class)
    except:
        with open(uiFile, 'r' , encoding="utf-8") as f:
            o = StringIO()
            frame = {}
            
            uic.compileUi(f, o, indent=0)
            pyc = compile(o.getvalue(), '<string>', 'exec')
            exec (pyc,frame)
            
            form_class = frame['Ui_%s'%form_class]
            base_class = eval('%s'%widget_class)

    return (base_class,form_class)
