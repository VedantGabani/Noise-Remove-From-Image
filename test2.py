import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('salt.png')


kernel = np.ones((5,5),np.float32)/25
dst = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()