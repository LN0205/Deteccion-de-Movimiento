import cv2
import numpy as np
from coordfilt import cordfilt
import time
def draw_alert(image, center, radius, color=(0, 0, 255), thickness=-1):
    cv2.circle(image, center, radius, color, thickness)
def show_alert(image, message="Alert!", position=(25, 100)):
    cv2.rectangle(image, (725, 10), (960, 70), (0, 0, 255), -1) 
    cv2.putText(image, message, position, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)


cap = cv2.VideoCapture(r"E:\repos\yolov8_training\MOVEMENTDETECTINO\FILTRO4\atoro_filtro4.mp4")
frame_width = 960  
frame_height = 540
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter(r"E:\repos\yolov8_training\MOVEMENTDETECTINO\FILTRO4\atoro_filtro4RESULTADO.mp4", fourcc, fps, (frame_width, frame_height), True)
ret, frame = cap.read()
print(ret)
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (7, 7), 0)
gray_frame = cv2.resize(gray_frame, (frame_width, frame_height))
hmask, wmask=gray_frame.shape
for i in range(4):
    exm=cordfilt(i+1)
    puntos=exm.corde()
    print("Coordenadas para el filtro:", i+1)
    print(puntos)
    umb=exm.umbral()
'''
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (frame_width, frame_height))
    start_time = time.time()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    frame_diff = cv2.absdiff(gray_frame, gray)
    _, thresh = cv2.threshold(frame_diff, umb[0], 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
#------------------------------------------------
#Antihorario
    puntos=exm.corde()
    pts = np.array(puntos, dtype=np.int32)
    mask = np.zeros(thresh.shape, dtype=np.uint8)
    #rect = cv2.boundingRect(pts)
    cv2.fillPoly(mask, [pts], 255)
    result = cv2.bitwise_and(thresh, mask)
    non_zero_count = np.count_nonzero(result)
    #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Pixeles detectados :",non_zero_count)
    coloresult=cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
    bool_mask = mask != 0
    frame[bool_mask] = coloresult[bool_mask]
    event_occurred=True
    if non_zero_count>umb[1]:
        #draw_alert(frame, (850, 50), 25) 
        show_alert(frame, "Alerta", (750, 50))
#-------------------------------------------------
    out.write(frame)
    #print(fps)
    cv2.imshow('Inverted Movement Detection', frame)
    gray_frame=gray
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
'''

