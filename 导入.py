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

# 爬取主要数据
url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341027523371041305267_1592721097964&_=1592721097965'
response=requests.get(url).text
first_index=response.find('(')
response=response[first_index+1:-1] #删掉得到数据中的无用部分
data=json.loads(response)['data']
data=json.loads(data)['areaTree'][0]['children']  # 得到一个列表，里面是我们需要的信息
province=[]  # 疫情地区
today_add=[]  # 新增
nowConfirm=[]  # 现有
for i in data:
    province.append(i['name'])  # 疫情地区
    today_add.append(i['today']['confirm'])  # 新增
    nowConfirm.append(i['total']['nowConfirm'])  # 现有
