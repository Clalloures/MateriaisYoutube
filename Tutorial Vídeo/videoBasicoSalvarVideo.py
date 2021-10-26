import cv2

captura = cv2.VideoCapture(0)
saida = cv2.VideoWriter(
    'videoFinal.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

while(captura.isOpened()):
    # O primeiro é um booleano ou seja retorna verdadeiro ou falso, enquanto o segundo é o frame do vídeo
    confirma_recebimento, frame = captura.read()
    if confirma_recebimento == True:
        cv2.imshow('video', frame)
        saida.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
saida.release()
cv2.destroyAllWindows()
