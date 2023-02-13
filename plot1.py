import matplotlib.pyplot as plt

x1 = [1, 5, 9, 13, 17, 2, 6, 10, 14, 18]
y1 = [5, 30, 15, 35, 5, 6, 31, 16, 36, 6]
# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 1")

x2 = [3, 8, 12, 16, 20,4,9,13,17,21]
y2 = [8, 33, 18, 38, 8,9,34,19,39,9]
# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(x2, y2, color='blue', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 2")

plt.xlim(0, 50) # 設定 x 軸座標範圍
plt.ylim(0, 50) # 設定 y 軸座標範圍

plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題內容及大小
plt.title('Plot title', fontsize="18") # 設定圖表標題內容及大小

plt.legend()
plt.show()
