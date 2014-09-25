import cv2
import numpy as np
import sys

arq = sys.argv[-1]

print(str(arq).split('/')[-1].split('.')[0])

ids = (str(arq).split('/')[-1].split('.')[0].split('-')[5:])

matrix_rgb = cv2.imread(str(arq))
matrix_gray = cv2.cvtColor(matrix_rgb, cv2.COLOR_BGR2GRAY)
w, h = matrix_gray.shape[::-1]

for count in range(0,len(ids)):
    newName = '-'.join(str(arq).split('/')[-1].split('.')[0].split('-')[0:5])
    newName = newName + '-' + ids[count] + '.jpg'
    cropedImage = matrix_rgb[int(count)*1000:int(count +1)*1000, 0:w]
    newName = '/'.join(str(arq).split('/')[0:-1]) + '-CROP/' + newName
    print newName
    cv2.imwrite(newName, cropedImage)