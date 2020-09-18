from quxpy import metro
import time
def foo():
    print("foo")

def bar():
    print("bar")

metro.add(foo, 1.0)  # name, func, interval in sec
metro.add(bar, 0.5)

try:
    metro.start(use_process=True)        

    while True:
        print("main loop")  
        time.sleep(1)

except KeyboardInterrupt:    
    metro.terminate()


