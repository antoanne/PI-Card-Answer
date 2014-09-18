import cv2
import numpy as np
threshold = 0.7


'''GET ANSWER'''
count = 45
options = ['a', 'b', 'c', 'd', 'e']

question_a = cv2.imread('templates/a.jpg')
question_a_gray = cv2.cvtColor(question_a, cv2.COLOR_BGR2GRAY)
question_a_w, question_a_h = question_a_gray.shape[::-1]

question_b = cv2.imread('templates/b.jpg')
question_b_gray = cv2.cvtColor(question_b, cv2.COLOR_BGR2GRAY)

question_c = cv2.imread('templates/c.jpg')
question_c_gray = cv2.cvtColor(question_c, cv2.COLOR_BGR2GRAY)

question_d = cv2.imread('templates/d.jpg')
question_d_gray = cv2.cvtColor(question_d, cv2.COLOR_BGR2GRAY)

question_e = cv2.imread('templates/e.jpg')
question_e_gray = cv2.cvtColor(question_e, cv2.COLOR_BGR2GRAY)

questions = { 'a': question_a_gray, 'b': question_b_gray, 'c': question_c_gray, 'd': question_d_gray, 'e': question_e_gray }

q = 0
respoastas = ''
while (q < count):
    q += 1
    #print "question " + str(q)
    question_rgb = cv2.imread('result/question_' + str(q) + '.jpg')
    question_gray = cv2.cvtColor(question_rgb, cv2.COLOR_BGR2GRAY)
    question_w, question_h = question_gray.shape[::-1]
    resposta = [None, None]
    for option in options:
        res = cv2.matchTemplate(question_gray, questions[option], cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        if(option == 'a'):
            resposta = [option, len(zip(*loc[::-1]))]
        else:
            if(resposta[1] > len(zip(*loc[::-1]))):
                resposta = [option, len(zip(*loc[::-1]))]
        #print "   " + str(option) + "::" + str(len(zip(*loc[::-1])))
    #print resposta
    print "question " + str(q) + " resposta (" + resposta[0].upper() + ")"
    respoastas += resposta[0].upper()
print respoastas






        #for pt in zip(*loc[::-1]):
        #print str(option) + "::" + str(pt)


        #cv2.rectangle(question_gray, (pt[0] - (w/5),0), (pt[0] + w, h2), (0,0,255), -1)


        #print str(option) + "::" + str(len(zip(*loc[::-1])))

        #q += 1
        #question = table_gray[ (q-1) * (h/q_count) : q *((h-2)/q_count), 0: w ]
        #cv2.imwrite('result/question_' + str(q + ((t-1)*q_count)) + '.jpg', question)
        #cv2.imshow('result',question)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #print "question " + str(q + ((t-1)*q_count))
