import cv2

captura = cv2.VideoCapture(2)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
saida = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480), 0)

while(captura.isOpened()):
    # O primeiro é um booleano ou seja retorna verdadeiro ou falso, enquanto o segundo é o frame do vídeo
    confirma_recebimento, frame = captura.read()
    if confirma_recebimento == True:
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', img_gray)
        saida.write(img_gray)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
saida.release()
cv2.destroyAllWindows()
