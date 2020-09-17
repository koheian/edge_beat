from PIL import Image
import numpy as np
from quxpy import osc_sender
import get_array

# configure remote address and port 
osc_sender.setup("127.0.0.1", 50000)
# test
osc_sender.send("/foo", 0.1, 0.2)
# open an edge image
#img = np.array(Image.open('laplacian.jpg'))
img = np.array(Image.open('canny.jpg'))

# get buffer
beat_list = get_array.get_beat_list(get_array.get_row_array("laplacian.jpg", 500), 128)

# send messege
osc_sender.send("/list", beat_list)
#print(type(beat_list[1]))
