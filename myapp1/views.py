from django.shortcuts import render
from django.http import request

# Create your views here.

from apscheduler.scheduler import Scheduler
# Start the scheduler
sched = Scheduler()
sched.start()

@sched.interval_schedule(seconds=2)
def getdata():
    print("hello view")

