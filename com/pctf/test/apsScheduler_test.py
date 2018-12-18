from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def timedTask():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    # 创建scheduler
    scheduler = BackgroundScheduler()
    # 添加时间间隔任务
    scheduler.add_job(timedTask, 'interval', seconds = 2)
    scheduler.start()

    while True:
        time.sleep(5)