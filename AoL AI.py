import pywhatkit
import pyautogui
import time

import cv2
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(1)

def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

abc = [0, 255, 255]

while True:
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimmit, upperLimit = get_limits(color=abc)

    mask = cv2.inRange(hsvImage, lowerLimmit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        pywhatkit.sendwhatmsg_to_group_instantly("DUS6s5zPesZ132MotSoVlo","! terjadi kebakaran !\n\n Lokasi:Kampus Binus Bekasi, Jalan Lingkar Boulevar Blok WA No.1 Summarecon Bekasi Kel, RT.006/RW.003, Marga Mulya, Kec. Bekasi Utara, Kota Bks, Jawa Barat 17142",10)
        time.sleep(1)
        pyautogui.press('enter')
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()