import time
 
 
def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec
 
 
# 时间间隔
second = sleep_time(0, 0, 4)
while True:
    time.sleep(second)
    print('hello world!')
 