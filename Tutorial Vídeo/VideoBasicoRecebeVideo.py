import cv2

captura = cv2.VideoCapture('videoFinal.avi')

while(captura.isOpened()):
    # O primeiro é um booleano ou seja retorna verdadeiro ou falso, enquanto o segundo é o frame do vídeo
    confirma_recebimento, frame = captura.read()
    if confirma_recebimento == True:
        cv2.imshow('video', frame)

        if cv2.waitKey(40) & 0xFF == ord('x'):
            break

captura.release()
cv2.destroyAllWindows()
