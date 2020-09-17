from PIL import Image
import numpy as np

def get_row_array(input_filename, raw_number):
    img = np.array(Image.open(input_filename))
    row_array = img[raw_number]
    return row_array

def get_beat_list(long_array, list_size):
    return long_array[0:list_size].tolist()
    
    
