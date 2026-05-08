# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:03:02 2020

@author: rohit
"""

import cv2
import matplotlib.pyplot as plt
from scipy import signal

original = cv2.imread("textured.jpg")
duplicate = cv2.imread("sunburst.jpg")

sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
kp_2, desc_2 = sift.detectAndCompute(duplicate, None)

index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc_1, desc_2, k=2)

good_points = []
ratio = 0.6
for m, n in matches:
    if m.distance < ratio*n.distance:
        good_points.append(m)
        print(len(good_points))
result = cv2.drawMatches(original, kp_1, duplicate, kp_2, good_points, None)
plt.imsave('Point_matching_diff_space.png', result)


cor = signal.correlate2d (original[:,:,0], duplicate[:,:,0])
