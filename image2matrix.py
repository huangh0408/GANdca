from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im=Image.open('random.jpg')
width,height=im.size
#im=im.convert("L")
#data=im.getdata()
#data=np.matrix(data,dtype='float')/255.0
#new_data=np.reshape(data,(height,width))
arr=np.array(im)
