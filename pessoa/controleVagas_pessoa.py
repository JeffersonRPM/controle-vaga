import cv2
import numpy as np

# Vagas mapeadas
#         x,  y,  w,   h
vaga1 = [630, 0, 300, 586]
vaga2 = [340, 0, 280, 586]

vagas = [vaga1, vaga2]

video = cv2.VideoCapture('C:/Users/gusta/Desktop/projeto_controle_vagas/pessoa/video1.mp4')

while True:

    check, img = video.read()

    if not check:
        print("Fim.")
        break

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # binarizando a img
    # desconsiderando ruidos                          md ponderada de px vizinhos     escuros p/ claros
    thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 15)

    # suavizando a imagem
    mdBlur = cv2.medianBlur(thresh, 5)

    # filtragem convolucional
    kernel = np.ones((3,3), np.int8)

    # expande as regiões brancas na imagem 
    dilate = cv2.dilate(mdBlur, kernel)

    qtdVagas = 0


    for x,y,w,h in vagas:
        recorte = dilate[y:y+h, x:x+w]
        qtdPxBranco = cv2.countNonZero(recorte)
        cv2.putText(img, str(qtdPxBranco), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        if qtdPxBranco > 10000:
                                                  #vermelho  w=3px
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
        else: 
                                                    #verde   w=3px
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
            qtdVagas += 1

    cv2.rectangle(img, (65,15), (210,60), (0,0,0), -1)
    cv2.putText(img, f'Vagas: {qtdVagas}/2', (75,45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 1)
             
    cv2.imshow('video thresh', dilate)
    cv2.imshow('video', img)
    cv2.waitKey(30)

