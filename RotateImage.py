import cv2
import numpy as np
import sys
import os

folder = sys.argv[1]

for filename in os.listdir(folder):
    if((filename != ".DS_Store") and (len(filename) >= 10)):
        print(len(filename), filename)
        img = cv2.imread(str(folder) + str(filename),0)
        rows,cols = img.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),-1,1)
        dst = cv2.warpAffine(img,M,(cols,rows))

        cv2.imwrite(str(folder) + str(filename), dst)
'''
cv2.imshow('result',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''