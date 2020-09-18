from quxpy import simple_event as event
import time, random

def foo():
    time.sleep(1)
    print(87)

def bar(*args):
    time.sleep(3)
    print(args)

def waiter(t):
    print("Start waiting for " + str(t) + " seconds.")
    time.sleep(t)
    print("finish waiting for " + str(t) + " seconds.")

event.add("foo", foo)
event.add("bar", bar)
event.add("/waiter", waiter)

event.bang("foo")
event.bang("bar", 1)

for i in range(100):
    event.bang("/waiter", random.randint(5, 10))
