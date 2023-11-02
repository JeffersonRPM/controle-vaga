import cv2

img = cv2.imread("C:/Users/gusta/Desktop/projeto_controle_vagas/selectROI/img1.jpg")

roi = cv2.selectROI("Selecione uma ROI", img)

# Feche a janela após a seleção
cv2.destroyWindow("Selecione uma ROI")

# Imprima as coordenadas da área: (x, y, largura, altura)
print(roi)
   