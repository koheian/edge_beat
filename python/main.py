from PIL import Image
import numpy as np
from quxpy import osc_sender
from quxpy import metro
import config
import get_array
import time
interval = 0.2
pixel_x = 0
pixel_y = 0

# open an edge image
image_filenames = ['laplacian.jpg', 'canny.jpg', 'sobel.jpg']
img = np.array(Image.open(image_filenames[0]))
# configure remote address and port 
osc_sender.setup("127.0.0.1", 50001)
# test
osc_sender.send("/foo", 0.1, 0.2)

# setup metro
def send_int():
    """
    画像のある列を選び、画素値の配列を得る。
    それがしきい値以上ならそのままを、それ以下ならNOTE_OFFをvelocityとして送る。
    """
    global pixel_x
    global pixel_y
    TH_NOTE = 34
    STAT_ON = 144
    STAT_OFF = 128
    VELO_MAX = 127
    VELO_NOTE_ON = 80 # 適当なvelocity
    VELO_NOTE_OFF = 0
    # get buffer
    velo_int = get_array.get_beat_int(get_array.get_row_array(img, pixel_y), pixel_x)

    # normalize the int
    velo_int = velo_int >> 1

    if velo_int > VELO_MAX:
        velo_int = VELO_MAX
        osc_sender.send("WARNING: velo is exceeded")
    elif velo_int > TH_NOTE:
        stat_int = STAT_ON
        #velo_int = VELO_NOTE_ON
    else:
        stat_int = STAT_OFF
        velo_int = VELO_NOTE_OFF

    osc_sender.send("/velo", velo_int)
    osc_sender.send("/stat", stat_int) # stat should be send at last

    pixel_x = (pixel_x + 1) % config.l_img

metro.add(send_int, interval)
# send messege
try:
    metro.start(use_process=False) 
    while True:
        time.sleep(1)
except KeyboardInterrupt:    
    metro.terminate()