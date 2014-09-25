import cv2
import numpy as np
import sys

arq = sys.argv[-1]

sys.stdout.write('\n' + str(arq).split('/')[-1].split('.')[0])

threshold = 0.2
max = 3

matrix_rgb = cv2.imread(str(arq))
matrix_gray = cv2.cvtColor(matrix_rgb, cv2.COLOR_BGR2GRAY)
w2, h2 = matrix_gray.shape[::-1]
newx,newy = matrix_rgb.shape[1]/3, matrix_rgb.shape[0]/3

template = cv2.imread('templates/table15_home.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

count = 0

def splitTable():
    global count
    
    res = cv2.matchTemplate(matrix_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold )
    for pt in zip(*loc[::-1]):
        count += 1
        img_croped = matrix_gray[0:h2, pt[0]- (w/6):pt[0] + w]
        cv2.imwrite('result/matrix_' + str(((pt[0])/(w2/4))+1) + '.jpg',img_croped)
        cv2.rectangle(matrix_gray, (pt[0],0), (pt[0] + w, h2), (0,0,255), -1)
        #print 'table ' + str(pt) + ' h' + str(h) + ' w' + str(w) + ' :: ' + str(((pt[0])/(w2/4))+1)
        break

    if (len(zip(*loc[::-1])) > 0):
        splitTable()

splitTable()
#print (str(count) + " tables")


'''QUESTIONS'''
threshold = 0.5
q_template = cv2.imread('templates/question_full_home.jpg')
q_template_gray = cv2.cvtColor(q_template, cv2.COLOR_BGR2GRAY)
w, h = q_template_gray.shape[::-1]
q_count = 0
count = 3
def splitQuestions():
    global q_count
    res = cv2.matchTemplate(matrix_croped_gray,q_template_gray,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold )
    #print loc
    #print zip(*loc[::-1])
    
    matrix_croped = None
    for pt in zip(*loc[::-1]):
        q_count += 1
        matrix_croped = matrix_croped_gray[ pt[1]:pt[1] + (50*16), 0: pt[0] + w2 ]
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
        
'''if (cropedImage != None):
        newx,newy = matrix_croped_rgb.shape[1]/3,matrix_croped_rgb.shape[0]/3
        img_rgb_small = cv2.resize(matrix_croped_gray,(newx,newy))
        cv2.imshow('result',cropedImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
