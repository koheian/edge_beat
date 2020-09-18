from quxpy import osc_sender
import random, time

# configure remote address and port 
osc_sender.setup("127.0.0.1", 50000)

# simple way
osc_sender.send("/foo", 0.1, 0.2)

# any nested params are available
params=[1, [2, 3] , ( [(4,5),6.2] ,7,8, "bar") ]
osc_sender.send("/foo", params)
