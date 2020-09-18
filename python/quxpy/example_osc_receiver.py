from quxpy import osc_receiver
import time

def foo(*args):
    time.sleep(2)
    print(args)

def bar(*args):
    print(args)


try:
    osc_receiver.setup(50001)   # set the listen port
    osc_receiver.add("/bar", bar)   # combine the OSC address and function 
    osc_receiver.add("/foo", foo)   # add another

    osc_receiver.start()    # begin server

    while True: # main loop
        print("sushi")
        time.sleep(5.0)

except KeyboardInterrupt:
    osc_receiver.terminate()