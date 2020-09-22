from PIL import Image
import numpy as np

def get_row_array(img, raw_number):
    #img = np.array(Image.open(input_filename))
    row_array = img[raw_number]
    return row_array

def get_beat_list(long_array, i_start, len_list):
    return long_array[i_start:(i_start+len_list)].tolist()
 
def get_beat_int(long_array, index):
    a = long_array[index].tolist()
    return a
