import matplotlib

import matplotlib.pyplot as plt

# import字型管理套件

from matplotlib.font_manager import FontProperties

import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB',
'weight' : 'bold',
'size'  : '16'}
plt.rc('font', **font) # pass in the font dict as kwargs
plt.rc('axes',unicode_minus=False)
 

# 指定使用字型和大小

myFont = FontProperties(fname='D:/python/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/STIXNonUni.ttf', size=14)

 

# 分類類型

category = ['便利商店', '百貨公司', '政府規費', '小吃美食', '餐廳', '大賣場']

# 每月總花費

expend = [1320, 3200, 500, 6000, 5800, 3900]

# 設定顏色

color = ['#ff0000', '#d200d2', '#66b3ff', '#28ff28', '#ffff37', '#5b00ae']

 

# 設定圓餅圖大小

plt.figure(figsize=(12,8))

# 依據類別數量，分別設定要突出的距離

separeted = (0, 0, 0.3, 0, 0, 0)      

 

# 設定圓餅圖屬性

pictures,category_text,percent_text = plt.pie(

        expend,                           # 數值

        colors = color,                   # 指定圓餅圖的顏色

        labels = category,                # 分類的標記

        autopct = "%0.2f%%",              # 四捨五入至小數點後面位數

        explode = separeted,              # 設定分隔的區塊位置

        pctdistance = 0.65,               # 數值與圓餅圖的圓心距離

        radius = 0.7,                     # 圓餅圖的半徑，預設是1

        center = (-10,0),                 # 圓餅圖的圓心座標

        shadow=False)                     # 是否使用陰影

 # 把每個分類設成中文字型

for t in category_text:

    t.set_fontproperties(font)

# 把每個數值設成中文字型

for t in percent_text:

    t.set_fontproperties(font)

   

# 設定legnd的位置

plt.legend(loc = "center right", prop=font)

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title("Python 畫圓餅圖(Pie chart)範例", fontproperties=font, x=0.5, y=1.03)

# 畫出圓餅圖

plt.show()