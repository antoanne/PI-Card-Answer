import cv2
import numpy as np
threshold = 0.3


'''SPLIT QUESTIONS'''
count = 3
q_count = 15

t = 0

while (t < count):
    q = 0
    t += 1
    table_rgb = cv2.imread('result/croped_questions' + str(t) + '.jpg')
    table_gray = cv2.cvtColor(table_rgb, cv2.COLOR_BGR2GRAY)
    w, h = table_gray.shape[::-1]
    while (q < q_count):
        q += 1
        question = table_gray[ (q-1) * (h/q_count) : q *((h-2)/q_count), 0: w ]
        cv2.imwrite('result/question_' + str(q + ((t-1)*q_count)) + '.jpg', question)
        #cv2.imshow('result',question)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        print "question " + str(q + ((t-1)*q_count))
