import numpy as np
import cv2
from matplotlib import pyplot as plt
import time 

img = cv2.imread('tes.png')
time.sleep(20)
print img.shape



dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
