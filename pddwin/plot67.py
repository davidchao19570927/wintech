import schedule
import time
 
def run():
    print("I'm doing something...")
 
schedule.every(10).seconds.do(run)    # 每隔十分钟执行一次任务 
schedule.every(10).minutes.do(run)    # 每隔十分钟执行一次任务
schedule.every().hour.do(run)         # 每隔一小时执行一次任务
schedule.every().day.at("10:30").do(run)  # 每天的10:30执行一次任务
schedule.every().monday.do(run)  # 每周一的这个时候执行一次任务
schedule.every().wednesday.at("13:15").do(run) # 每周三13:15执行一次任务
 
while True:
    schedule.run_pending()  # run_pending：运行所有可以运行的任务
