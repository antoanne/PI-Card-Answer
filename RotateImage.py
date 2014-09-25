import cv2
import numpy as np
import sys

arq = sys.argv[1]

img = cv2.imread(arq,0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),-0.5,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite(arq, dst)
'''
cv2.imshow('result',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''