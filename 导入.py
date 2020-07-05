# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:02:29 2020

@author: dell
"""

from pyecharts.charts import Map # 用来画地图
from pyecharts import options as opts
import matplotlib; matplotlib.use('TkAgg') #用来画条形图
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager #因为有中文
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")  # 设置字体为微软雅黑

import requests
import re
import json
import math  # 正无穷，因为有个>=10000
import time