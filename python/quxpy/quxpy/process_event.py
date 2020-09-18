# multiprocess event handler

from multiprocessing import Process

events = {}
jobs = []

def add(event_name, func):
    global events
    events[event_name] = func

def bang(event_name, *args):
    global events, jobs
    func = events[event_name]

    job = Process(target=func, args=args)
    jobs.append(job)
    job.start()

def close():
    for job in jobs:
        job.join()
    
