from pythonosc import dispatcher, osc_server
from . import thread_event as event
from threading import Thread
from multiprocessing import Process

class OscReceiver:
    def __init__(self, port):
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", port), self.dispatcher)        

    def add(self, adr, func):
        event.add(adr, func)
        self.dispatcher.map(adr, event.bang)

    def loop(self):
        self.server.serve_forever()

    def start(self, use_process=False):
        if use_process:
            self.worker = Process(target=self.loop)                    
        else:
            self.worker = Thread(target=self.loop)                    
        self.worker.start()


    def terminate(self):        
        self.server.shutdown()
        self.worker.join()

receiver = None

def setup(port):
    global receiver
    receiver = OscReceiver(port)

def start(use_process=False):
    global receiver
    receiver.start(use_process)

def add(adr, func):
    global receiver
    receiver.add(adr, func)

def terminate():
    global receiver
    receiver.terminate()
    event.close()
