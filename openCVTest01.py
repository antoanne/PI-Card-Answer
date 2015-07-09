import cv2
import numpy as np
import sys

arq = sys.argv[-1]
#arq = "images/PI-2015-1BIM-1DIA-1001/02.JPG"

sys.stdout.write('\n' + str(arq).split('/')[-1].split('.')[0])

# 0.27
threshold = 0.40
max = 3

matrix_rgb = cv2.imread(str(arq))
matrix_gray = cv2.cvtColor(matrix_rgb, cv2.COLOR_BGR2GRAY)
w2, h2 = matrix_gray.shape[::-1]
newx,newy = matrix_rgb.shape[1]/3, matrix_rgb.shape[0]/3

template = cv2.imread('templates/table15.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

count = 0

def splitTable():
    global count
    
    res = cv2.matchTemplate(matrix_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold )
    #print loc
    for pt in zip(*loc[::-1]):
        count += 1
        img_croped = matrix_gray[0:h2, pt[0] - 70:pt[0] + w]
        cv2.imwrite('result/matrix_' + str(((pt[0])/(w2/4))+1) + '.jpg',img_croped)
        cv2.rectangle(matrix_gray, (pt[0],0), (pt[0] + w, h2), (0,0,255), -1)
        #print 'table ' + str(pt) + ' h' + str(h) + ' w' + str(w) + ' :: ' + str(((pt[0])/(w2/4))+1)
        break

    if (len(zip(*loc[::-1])) > 0):
        splitTable()

splitTable()
#print (str(count) + " tables")


#NEW QUESTIONS
#0.25
threshold = 0.37
q_count = 0
count = 3
def splitQuestions():
    global q_count
    res = cv2.matchTemplate(matrix_croped_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold )
    #print loc
    #print zip(*loc[::-1])

    matrix_croped = None
    for pt in zip(*loc[::-1]):
        q_count += 1
        #print "%d :: %d :: %d :: %d" % (pt[1], pt[0], w, h)
        #matrix_croped = matrix_croped_gray[ pt[1] + 60: pt[1] + h - 88, 0: pt[0] + w ]
        matrix_croped = matrix_croped_gray[ pt[1] + 15: pt[1] + h - 88, 0: w + 88 ]
        cv2.imwrite('result/croped_questions_' + str(q_count) + '.jpg',matrix_croped)
        #print 'question ' + str(pt) + ' h' + str(h) + ' w' + str(w)
        break
    #print (str(q_count) + " questions")
    #return matrix_croped

t = 0
while (t < count):
    t += 1
    matrix_croped_rgb = cv2.imread('result/matrix_' + str(t) + '.jpg')
    matrix_croped_gray = cv2.cvtColor(matrix_croped_rgb, cv2.COLOR_BGR2GRAY)
    w2, h2 = matrix_croped_gray.shape[::-1]
    cropedImage = splitQuestions()
