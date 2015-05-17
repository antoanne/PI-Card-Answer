import cv2
import numpy as np
import sys

arq = sys.argv[1]

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

def gravaRespostas(r):
    file = open("respostas.txt", "a")
    file.write(r)
    file.close()

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
    #print "question " + str(q) + " resposta (" + resposta[0].upper() + ")"
    respoastas += resposta[0].upper()
gravaRespostas(','.join(str(arq).split('/')[-2].split('-')) + ',' + str(arq).split('/')[-1].split('.')[0] + ',' + ','.join(respoastas) + '\n')
#print respoastas
sys.stdout.write('#OK#')

