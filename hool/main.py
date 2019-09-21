# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import sys,json,os,re,jieba,imageio,collections
import pandas as pd
import urllib.request
from pyecharts import Geo,Line,Bar
from pyecharts import Overlap
from wordcloud import  WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


#  热力图,主要城市评论数 显示界面
class MainWindows(QMainWindow):
    def __init(self):
        super(MainWindows, self).__init()
        self.setGeometry(200,200,1250,650)
        self.browser = QWebEngineView()

    def kk(self, title, hurl):
        self.setWindowTitle(title)
        url = d + '/' + hurl
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

#  词云显示界面
class MainWindowy(QMainWindow):
    def __init__(self):
        super(MainWindowy, self).__init__()
        self.setGeometry(200,200,650,650)
        self.browser = QLabel()

    def kk(self, title , hurl):
        self.setWindowTitle(title)
        url = d + '/' + hurl

        pixmap = QPixmap(url)
        scaredPixmap = pixmap.scaled(QSize(600,600), aspectRationMode = Qt.KeepAspectRatio)
        self.browser.setPixmap(scaredPixmap)
        self.browser.show()
        self.setCentralWidget(self.browser)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(433, 223)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 30, 261, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(93, 94, 235, 89))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #  隐藏查看内容
    def hide(self):
        self.pushButton_4.setVisible(False)
        self.label_4.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label_3.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_2.setVisible(False)

    # 显示查看内容
    def show(self):
        self.pushButton_4.setVisible(True)
        self.label_4.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.label_3.setVisible(True)
        self.label_2.setVisible(True)
        self.pushButton_2.setVisible(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "黄渤电影分析"))
        self.label.setText(_translate("Form", "选择电影："))
        self.comboBox.setItemText(0, _translate("Form", "夏洛特烦恼"))
        self.comboBox.setItemText(1, _translate("Form", "羞羞的铁拳"))
        self.comboBox.setItemText(2, _translate("Form", "西虹市首富"))
        self.pushButton.setText(_translate("Form", "分析"))
        self.label_2.setText(_translate("Form", "主要城市评论数-及平均分："))
        self.pushButton_2.setText(_translate("Form", "查看"))
        self.label_3.setText(_translate("Form", "                 热力图："))
        self.pushButton_3.setText(_translate("Form", "查看"))
        self.label_4.setText(_translate("Form", "                   云词："))
        self.pushButton_4.setText(_translate("Form", "查看"))
        # 绑定电影选择处理方法
        self.comboBox.activated[str].connect(self.itemchange)
        # 分析功能
        self.pushButton.clicked.connect(self.anal)
        # 判断是否有词云
        if not os.path.isfile(d + '夏洛特烦恼词云.png'):
            self.pushButton.setText('分析')
            self.hide()
        else:
            self.pushButton.setText('完成重新分析')
            self.moveName = '夏洛特烦恼'
            self.moveId = '246082'
            self.show()
            self.btnclick()

    # 绑定电影选择处理
    def itemchange(self, text):
        if text == '夏洛特烦恼':
            if not os.path.isfile(d + '夏洛特烦恼词云.png' ):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '夏洛特烦恼'
                self.moveId = '246082'
                self.show()
                self.btnclick()
        if text == '羞羞的铁拳':
            if not os.path.isfile(d + '羞羞的铁拳词云.png' ):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '羞羞的铁拳'
                self.moveId = '1198214'
                self.show()
                self.btnclick()
        if text == '西虹市首富':
            if not os.path.isfile(d + '西虹市首富词云.png' ):
                self.pushButton.setText('分析')
                self.hide()
            else:
                self.pushButton.setText('完成重新分析')
                self.moveName = '西虹市首富'
                self.moveId = '1212592'
                self.show()
                self.btnclick()

    # 查看按钮的绑定事件
    def btnclick(self):
        self.pushButton_2.clicked.connected(self.reli2)
        self.pushButton_3.clicked.connected(self.reli3)
        self.pushButton_4.clicked.connected(self.reli4)

    # 主要城市评论数 - 及平均分查看按钮事件
    def reli2(self):
        win.kk(self.moveName + '主要城市评论数及平均分', self.moveName + '主要城市评论数_平均分.html')
        win.show()

    # 全国热图查看按钮点击事件
    def reli3(self):
        win.kk(self.moveName + '全国热力图', self.moveName + '全国热力图.html')
        win.show()

    # 词云查看按钮点击事件
    def reli4(self):
        winy.kk(self.moveName + '词云', self.moveName + '主要城市评论数_平均分.png')
        winy.show()

    def  anal(self):
        if self.comboBox.currentIndex() == 0:
            self.moveName = '夏洛特烦恼'
            self.moveId = '246082'
            self.getData()
        if self.comboBox.currentIndex() == 1:
            self.moveName = '羞羞的铁拳'
            self.moveId = '1198214'
            self.getData()
        if self.comboBox.currentIndex() == 2:
            self.moveName = '西红柿首富'
            self.moveId = '1212592'
            self.getData()
        self.show()
        self.pushButton.setText('完成重新分析')
        self.btnclick()

    # 获取评论的json文件并分析
    def getData(self):
        tomato = pd.DataFrame(columns=['date', 'score', 'city', 'comment', 'nick'])
        i = 1
        while True:
            print(i)
            try:
                url = 'http://m.maoyan.com/mmdb/comments/movie/' + self.moveId + '.json?_v_ = yes&offset=' + str(i)
                html = urllib.request.urlopen(url)
                content = html.read()
                # print(content)
                total = json.loads(content)['total']
                print(total)
                if total == 0:
                    break
                else:
                    data = json.loads(content)['cmts']
                    datah = json.loads(content)['hcmts']
                    for item in data:
                        tomato = tomato.apennd({'date': item['time'].split(' ')[0],
                                                'city': item['cityName'],
                                                'score': item['score'],
                                                'comment': item['content'],
                                                'nick': item['nick']
                                                }, ignore_index=True)
                    for item in datah:
                        tomato = tomato.apennd({'date': item['time'].split(' ')[0],
                                                'city': item['cityName'],
                                                'score': item['score'],
                                                'comment': item['content'],
                                                'nick': item['nick']
                                                }, ignore_index=True)
                    i = i + 1
            except:
                i += 1
                continue
        tomato = tomato.drop_duplicates(subset=['date', 'score', 'city', 'comment', 'nick'], keep='first')
        tomato.to_excel(self.moveName + '.xlsx', sheet_name='data')

        tomato_com = pd.read_excel(self.moveName + '.xlsx')          # 存好以后读文件
        grouped = tomato_com.groupby(['city'])
        grouped_pct = grouped['score']
        city_com = grouped_pct.agg(['mean','count'])
        city_com.reset_index(inplace = True)
        city_com['mean'] = round(city_com['mean'],2)
        geo = Geo('《'+ self.moveName + '》 全国热力图' ,
                  title_color = '#fff',
                  title_pos = 'center',
                  width = 1200,
                  height = 600,
                  background_color = '#404a59'
                  )
        flag = True
        data = [(city_com['city'][i] , city_com['count'][i]) for i in range(0, city_com.shape[0])]
        while flag:
            attr, value = geo.cast(data)
            try:
                geo.add('',attr, value,
                        type = 'heatmap',
                        visual_range = [0,50],
                        visual_text_color = '#fff',
                        symbol_size = 15,
                        is_visualmap = True,
                        is_roam = False
                        )
                flag = False
            except ValueError as e:
                e = str(e)
                e = e.split('No coordinate is specified for ')[1]  # 获取不支持的城市名
                for i in range(0, len(data)):
                    if e in list(data[i]):
                        del data[i]
                        break
                    flag = True


        # 生成热力图html文件
        geo.render(d + self.moveName + '全国热力图.html')
        city_main = city_com.sort_values('count', ascending = False)[0:30]
        attr = city_main['city']
        v1 = city_main['count']
        v2 = city_main['mean']
        line = Line('主要城市评分')
        line.add('城市',attr, v2,
                 is_stack = True,
                 xaxis_rotate= 30,
                 yaxis_min = 0,
                 mark_point=['min','max'],
                 line_color= 'lightblue',
                 xaxis_interval = 0,
                 line_width = 4,
                 mark_point_textcolor= 'black',
                 mark_point_color = 'lightblue',
                 is_splitline_show = False
                 )
        bar = Bar('主要城市评论数')
        bar.add('城市',attr, v1,
                is_stack = True,
                xaxis_rotate= 30,
                yaxis_min=0,
                xaxis_interval=0,
                is_splitline_show= False
                )
        overlap = Overlap()
        overlap.add(bar)
        overlap.add(line, yaxis_index=1, is_add_yaxis= True)
        overlap.render(d + self.moveName + '主要城市评论数_平均分.html')
        print('主要城市评论：', d + self.moveName + '主要城市评论数_平均分.html' )
        tomato_str = ' '.join(tomato_com['comment'])
        words_list = []

        words_list = []
        word_generator = jieba.cut_for_search(tomato_str)
        for word in word_generator:
            words_list.append(word)
        words_list = [k for k in words_list if len(k)>1]
        back_color = imageio.imread(d + '词云背景.jpg')  # 图片解析
        wc = WordCloud(background_color= 'white',
                       max_words= 200,
                       mask = back_color,  # 以该参数作图绘制词云，参数不为空，width和height会忽略
                       max_font_size = 300, # 显示字体最大值
                       font_path = 'STFANGSO.ttf',  # 字体
                       random_state = 42  # 为每个词返回PTL颜色
        )
        tomato_count = collections.Counter(words_list)
        wc.generate_from_frequencies(tomato_count)
        image_colors = ImageColorGenerator(back_color) # 基于彩色图像生成相应彩色
        plt.figure() # 绘制词云
        plt.imshow(wc.recolor(color_func = image_colors))
        plt.axes('off') # 去掉坐标轴
        wc.to_file(os.path.join(d, self.moveName + '词云.png'))
        pass

if __name__ == '__main__':
    # 定义获取文件路径
    d = os.path.dirname(os.path.realpath(sys.argv[0])) + '/'
    d = re.sub(r'\\','/', d)

    app = QtWidgets.QApplication(sys.argv)   # 实例化QApplication类
    MainWindow = QtWidgets.QMainWindow()
    win = MainWindows()       # 热力图及主要城市评论数显示
    winy = MainWindowy()      # 词云界面显示
    ui = Ui_Form()            # 初始化主窗体
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







