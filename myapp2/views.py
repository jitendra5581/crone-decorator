from django.shortcuts import render
from apscheduler.scheduler import Scheduler


# Start the scheduler
sched = Scheduler()
sched.start()



@sched.interval_schedule(seconds=2)
def getapp2data():
    print("hello view2")