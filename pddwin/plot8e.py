from highcharts import Highchart 
chart = Highchart() 


#name: 'Hestavollane',
data01 = [4.3, 5.1, 4.3, 5.2, 5.4, 4.7, 3.5, 4.1, 5.6, 7.4, 6.9, 7.1,
          7.9, 7.9, 7.5, 6.7, 7.7, 7.7, 7.4, 7.0, 7.1, 5.8, 5.9, 7.4,
          8.2, 8.5, 9.4, 8.1, 10.9, 10.4, 10.9, 12.4, 12.1, 9.5, 7.5,
         7.1, 7.5, 8.1, 6.8, 3.4, 2.1, 1.9, 2.8, 2.9, 1.3, 4.4, 4.2,
         3.0, 3.0]

#name: 'Voll',
data02 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.3, 0.0,
          0.0, 0.4, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
          0.0, 0.6, 1.2, 1.7, 0.7, 2.9, 4.1, 2.6, 3.7, 3.9, 1.7, 2.3,
          3.0, 3.3, 4.8, 5.0, 4.8, 5.0, 3.2, 2.0, 0.9, 0.4, 0.3, 0.5, 0.4]

chart.add_data_set(data01,'spline',name='Hestavollane')
chart.add_data_set(data02, 'spline', name='Voll')
options = {
    "title": {
       "text": '風速變化趨勢圖'
             },
    "subtitle": {
        "text": '2009年10月6日和7日兩地風速情況'
        },
   "xAxis": {
      "type": 'datetime',
      "labels": {
      "overflow": 'justify'
          }
        },
   "yAxis": {
      "title": {
        "text": '風 速 (m/s)'
          },
  "min": 0,
  "minorGridLineWidth": 0,
  "gridLineWidth": 0,
  "alternateGridColor": None,
  "plotBands": [{ #// Light air
   "from": 0.3,
   "to": 1.5,
   "color": 'rgba(68, 170, 213, 0.1)',
   "label": {
    "text": '輕空氣',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// Light breeze
   "from": 1.5,
   "to": 3.3,
   "color": 'rgba(0, 0, 0, 0)',
   "label": {
    "text": '微風',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// Gentle breeze
   "from": 3.3,
   "to": 5.5,
   "color": 'rgba(68, 170, 213, 0.1)',
   "label": {
    "text": '柔和風',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// Moderate breeze
   "from": 5.5,
   "to": 8,
   "color": 'rgba(0, 0, 0, 0)',
   "label": {
    "text": '溫和風',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// Fresh breeze
   "from": 8,
   "to": 11,
   "color": 'rgba(68, 170, 213, 0.1)',
   "label": {
    "text": '清新風',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// Strong breeze
   "from": 11,
   "to": 14,
   "color": 'rgba(0, 0, 0, 0)',
   "label": {
    "text": '強風',
    "style": {
     "color": '#606060'
    }
   }
  }, { #// High wind
   "from": 14,
   "to": 15,
   "color": 'rgba(68, 170, 213, 0.1)',
   "label": {
    "text": '狂風',
    "style": {
     "color": '#606060'
    }
   }
  }]
 },
 "tooltip": {
  "valueSuffix": ' m/s'
 },
 "plotOptions": {
  "spline": {
   "lineWidth": 4,
   "states": {
    "hover": {
     "lineWidth": 5
    }
   },
   "marker": {
    "enabled": False
   },
   "pointInterval": 3600, #// one hour
   
  }
 } 
}

chart.set_dict_options(options)
chart
chart.save_file()