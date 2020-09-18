from PIL import Image
import numpy as np

img = np.array(Image.open('sobel.jpg'))

print(img.shape)
