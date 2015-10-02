import cv2
import numpy as np
import sys
import os

folder = sys.argv[-1]

sys.stdout.write('\n' + str(folder).split('/')[-1])



template = cv2.imread('templates/header.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
tw, th = template_gray.shape[::-1]

template_number = cv2.imread('templates/header.jpg')
template_number_gray = cv2.cvtColor(template_number, cv2.COLOR_BGR2GRAY)
tNw, tNh = template_number_gray.shape[::-1]

template_ball = cv2.imread('templates/ball.jpg')
template_ball_gray = cv2.cvtColor(template_ball, cv2.COLOR_BGR2GRAY)
bw, bh = template_ball_gray.shape[::-1]
    
for filename in os.listdir(folder):
    print(filename)
    if((filename != ".DS_Store") and (len(filename) >= 10)):
        try:
            dezena = 0
            unidade = 0
            matrix_rgb = cv2.imread(str(folder) + str(filename))
            matrix_gray = cv2.cvtColor(matrix_rgb, cv2.COLOR_BGR2GRAY)
            w, h = matrix_gray.shape[::-1]
            threshold = 0.20
            res = cv2.matchTemplate(matrix_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold )

            for pt in zip(*loc[::-1]):
                #print pt
                img_croped = matrix_gray[pt[1]:pt[1] + th + 130, pt[0]:pt[0] + tw]
                cv2.imwrite('result/header.jpg',img_croped)
                break

            header = cv2.imread('result/header.jpg')
            header_gray = cv2.cvtColor(header, cv2.COLOR_BGR2GRAY)
            tHNw, tHNh = header_gray.shape[::-1]
            threshold = 0.19
            res = cv2.matchTemplate(header_gray, template_number_gray, cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold )

            for pt in zip(*loc[::-1]):
                #print pt
                #header_croped = header_gray[pt[1]:pt[1] + tNh, pt[0]:pt[0] + tNw]
                header_croped = header_gray[50:tNh, 180:820]
                cv2.imwrite('result/header_number.jpg',header_croped)
                break

            header_number = cv2.imread('result/header_number.jpg')
            header_number_gray = cv2.cvtColor(header_number, cv2.COLOR_BGR2GRAY)
            HNw, HNh = header_number_gray.shape[::-1]
            threshold = .4

            q_count = 10
            q = 0
            while (q < q_count):
                q += 1
                img_croped = header_number_gray[0:HNh/2, (65 * (q - 1)) + 3:(65 * q) + 3]
                #cv2.imwrite('result/header_number_crop' + str(q) + '.jpg',img_croped)
                res = cv2.matchTemplate(img_croped, template_ball_gray, cv2.TM_CCOEFF_NORMED)
                loc = np.where( res >= threshold )

                for pt in zip(*loc[::-1]):
                    dezena = (q, 0)[(q == 10)]
                    break

            q = 0
            while (q < q_count):
                q += 1
                img_croped = header_number_gray[HNh/2:HNh, (65 * (q - 1)) + 3:(65 * q) + 3]
                #cv2.imwrite('result/header_number_crop' + str(q) + '.jpg',img_croped)
                res = cv2.matchTemplate(img_croped, template_ball_gray, cv2.TM_CCOEFF_NORMED)
                loc = np.where( res >= threshold )

                for pt in zip(*loc[::-1]):
                    unidade = (q, 0)[(q == 10)]
                    break

            print str(dezena) + str(unidade)
            if not(os.path.isfile(str(folder) + str(dezena) + str(unidade) + '.JPG')):
                os.rename(str(folder) + str(filename), str(folder) + str(dezena) + str(unidade) + '.JPG')
            os.remove('result/header.jpg')
            os.remove('result/header_number.jpg')
        except:
            print filename
    