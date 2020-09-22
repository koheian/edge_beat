from PIL import Image
import numpy as np
from quxpy import osc_sender
from quxpy import metro
import config
import get_array
import time
interval = 0.5
i = 0

# open an edge image
image_filenames = ['laplacian.jpg', 'canny.jpg', 'sobel.jpg']
img = np.array(Image.open(image_filenames[0]))
# configure remote address and port 
osc_sender.setup("127.0.0.1", 50001)
# test
osc_sender.send("/foo", 0.1, 0.2)

# setup metro
def send_int():
    global i
    # get buffer
    beat_int = get_array.get_beat_int(get_array.get_row_array(img, 500), i)
    i = (i + 1) % config.l_img
    osc_sender.send("/note", beat_int)

metro.add(send_int, interval)
# send messege
try:
    metro.start(use_process=False) 
    while True:
        time.sleep(1)
except KeyboardInterrupt:    
    metro.terminate()