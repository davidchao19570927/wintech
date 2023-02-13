from highcharts import Highchart 
chart = Highchart() 

data01 = [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
data02 =[24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
data03 =[11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
data04 = [550, 780, 7988, 12169, 15112, 22452, 34400, 34227]
data05 = [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]

chart.add_data_set(data01,'line',name='安裝，實施人員')
chart.add_data_set(data02, 'line', name='工人')
chart.add_data_set(data03,'line',name='銷售')
chart.add_data_set(data04, 'line', name='專案開發')
chart.add_data_set(data05,'line',name='其他')

options = {
     "title": {
       "text": '2010 ~ 2016 年太陽能行業就業人員發展情況'},
    "subtitle": {
      "text": '資料來源：thesolarfoundation.com'},
    "yAxis": {
      "title": {
         "text": '就業人數'
        }},
     "legend": {
        "layout": 'vertical',
         "align": 'right',
         "verticalAlign": 'middle'
      }}
chart.set_dict_options(options)
chart
chart.save_file()