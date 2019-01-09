# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 05:40:47 2018

@author: King
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(*.jpg,cv2.IMREAD_GRAYSCALE)

image_enhanced = cv2.equalizeHist(image)

plt.imshow(image_enhanced,cmap='gray'),plt.axis("off")

plt.show()

cv2.imwrite('abc.jpg',image)