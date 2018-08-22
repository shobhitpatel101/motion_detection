# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:14:22 2018

@author: sumit
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgbg1=fgbg.apply(frame)
    cv2.imshow('',fgbg1)
    
    if cv2.waitKey(1) & 0xFF==ord('f'):
        break

cap.release()
cv2.destroyAllWindows()
