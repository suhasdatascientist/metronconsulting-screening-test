# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 06:00:01 2018

@author: King
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#image = cv2.imread(*.jpg,cv2.IMREAD_GRAYSCALE)
image_bgr = cv2.imread('6.jpeg')
image_gray = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2GRAY)
image_gray = np.float32(image_gray)
image_cropped = image_bgr[:,:]

plt.imshow(image_cropped,cmap='gray'),plt.axis("off")
plt.show()

block_size = 3
aperture = 28
free_parameter = 0.04


detector_response = cv2.cornerHarris(image_gray,block_size,aperture,free_parameter)
detector_responses = cv2.dilate(detector_response,None)

threshold = 0.02
image_bgr[detector_responses > threshold * detector_responses.max()]=[255,255,255]

image_gray = cv2.cvtColor(image_bgr,cv2.COLOR_BG2GRAY)
plt.imshow(image_gray,cmap='gray')
plt.show()


plt.imshow(image_cropped,cmap='gray'),plt.axis("off")
plt.show()

cv2.imwrite('xyz6.jpg',image_cropped)

