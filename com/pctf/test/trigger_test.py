from datetime import datetime, timedelta
import time
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler

def jon_func(text):
    print(text)
    print(datetime.now().strftime('%H:%M:%S'))

if __name__ == '__main__':
    scheduler = BackgroundScheduler()

    scheduler.add_job(jon_func, 'date', next_run_time=datetime.now() + timedelta(seconds=10), args=['why is next_run_time?'])

    scheduler.start()

    scheduler2 = BackgroundScheduler();

    cronStr = '*/5 * * * * * *'
    crons = cronStr.split(" ")

    cronjob = scheduler2.add_job(jon_func, 'cron', second=crons[0], minute=crons[1], hour=crons[2], day=crons[3],
                       month=crons[4], week=crons[5], year=crons[6], args=['cron test'], id='3')

    scheduler2.start()

    time.sleep(20)

    scheduler2.remove_job('3')

    time.sleep(10)

    print('job removed')