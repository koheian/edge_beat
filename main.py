from PIL import Image
import numpy as np
import osc_sender
import get_array

# configure remote address and port 
osc_sender.setup("127.0.0.1", 50000)
# open an edge image
img = np.array(Image.open('sobel.jpg'))

# get buffer
beat_list = get_array.get_beat_list(get_array.get_row_array("laplacian.jpg"), 128)

# send messege
osc_sender.send("/list", beat_list)
#print(type(beat_list[1]))