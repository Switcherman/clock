#!/usr/bin/env python3
import json
import sys
import time
import os

root_path = os.path.abspath(os.path.join(os.getcwd(), "../../"))
sys.path.append(root_path)
default_sound = os.path.join(root_path, "default.mp3")
config_file = os.path.join(root_path, "clockconfiguration.json")

from apscheduler.schedulers.background import BackgroundScheduler
from com.pctf.entity.clock import dict_to_clock
from com.pctf.event.clock_event import ring

'''this is a clock program for mac
    author: lucifer
    date: 2018-12-17
'''

def boot():
    args = sys.argv
    print(args)
    clocks = load_config(config_file)
    jobs, scheduler = init_scheduler(clocks)
    scheduler.start()
    while True:
        time.sleep(100)

# load clock config
def load_config(file):
    with open(file, 'r') as in_stream:
        config_array = json.loads(in_stream.read())
        return [dict_to_clock(config) for config in config_array]

# init scheduler
def init_scheduler(clocks):
    scheduler = BackgroundScheduler()
    jobs = list()
    for clock in clocks:
        if not clock.enabled:
            continue
        crons = clock.cron.split(" ")
        name = clock.name
        if clock.sound == 'default':
            clock.sound = default_sound
        jobs.append(scheduler.add_job(ring, 'cron', second=crons[0], minute=crons[1], hour=crons[2], day=crons[3],
                          month=crons[4], day_of_week=crons[5], args=[clock], id=str(len(jobs)), name=name))
    return jobs, scheduler

if __name__ == '__main__':
    boot()
