from quxpy import thread_event as event  # process_event behaves the same way
import time, random

def foo():
    time.sleep(1)
    print(1.23)

def bar(*args):
    time.sleep(3)
    print(args)

def waiter(t):
    print("Start waiting for " + str(t) + " seconds.")
    time.sleep(t)
    print("finish waiting for " + str(t) + " seconds.")



try:
    event.add("foo", foo)
    event.add("bar", bar)
    event.add("/waiter", waiter)


    event.bang("foo")
    event.bang("bar", 0.87)

    for i in range(10):
        event.bang("/waiter", random.randint(5, 10))
except KeyboardInterrupt:    
    event.close()
