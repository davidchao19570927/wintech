import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

root = Tk()
root.title("tkinter and matplotlib")

f = Figure(figsize=(5, 4), dpi=100)
f_plot = f.add_subplot(111)

def other_picture_alg(): #數據相關的算法應該與plot分離開
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 6, 9, 12, 15, 18, 15, 12, 15, 18]
    return x, y

def draw_picture():
    f_plot.clear()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #關於數據的部分可以提取出來
    y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    f_plot.plot(x, y)
    canvs.draw()

def draw_picture2():
    f_plot.clear()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #關於數據的部分可以提取出來
    y = [2, 4, 6, 8, 10, 8, 6, 4, 2, 0]
    f_plot.plot(x, y)
    canvs.draw()

def draw_picture3():
    f_plot.clear()
    x, y = other_picture_alg() # 使用由算法生成的數據，可以避免重複的運算過程
    f_plot.plot(x, y)
    canvs.draw()

canvs = FigureCanvasTkAgg(f, root)
canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
Button(root, text='pic', command=draw_picture).pack()
Button(root, text='pic2', command=draw_picture2).pack()
Button(root, text='pic3', command=draw_picture3).pack()

root.mainloop()