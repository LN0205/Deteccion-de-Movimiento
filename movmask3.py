import cv2
import numpy as np

cap = cv2.VideoCapture(r'E:\repos\yolov8_training\MOVEMENTDETECTINO\output.mp4')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('detecmov.mp4', fourcc, fps, (frame_width, frame_height), False)
ret, frame = cap.read()
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    frame_diff = cv2.absdiff(gray_frame, gray)
    _, thresh = cv2.threshold(frame_diff, 20, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
    
#------------------------------------------------
    binary_image = thresh
    x1, y1, x2, y2 = 3, 4, 1000, 1800
    mask = np.zeros_like(binary_image)
    mask[x1:x2,y1:y2] = 255  
    result = cv2.bitwise_and(binary_image, mask)
#-------------------------------------------------
    out.write(result)
    cv2.imshow('Inverted Movement Detection', result)
    gray_frame=gray
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()


