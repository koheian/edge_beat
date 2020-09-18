import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

events = []
metro_loop = None
executor = None

def add(func, interval):
    event = {
        "func":func,
        "interval": interval,
        "prev_time": time.time(),
    }

    events.append(event)

def update():
    for event in events:
        now = time.time()
        diff = now - event["prev_time"]
        
        if event["interval"] < diff:                        
            executor.submit(event["func"])
            event["prev_time"] = now

def update_loop():    
    while True:
        try:      
            update()
        except Exception:
            break

def start(use_process=False, num_processes=None, reset_timer=True):  
    global executor
    if use_process:
        executor = ProcessPoolExecutor(max_workers=num_processes)
    else:
        executor = ThreadPoolExecutor(max_workers=num_processes)
    
    if reset_timer:
        now = time.time()
        for event in events:
            event["prev_time"] = now
    
    global metro_loop
    metro_loop = threading.Thread(target=update_loop)

    metro_loop.start()


def terminate():
    executor.shutdown()
    metro_loop.join()    