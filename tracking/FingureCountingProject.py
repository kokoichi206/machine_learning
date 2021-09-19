import cv2
import time
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

# 各々の指の先端の id 
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []    # 1: close, 0: open
        # 親指のみ、x 座標の値で判定。左右どっちの手でもできるようにしてる
        if (lmList[2][1] - lmList[1][1]) * (lmList[4][1] - lmList[3][1]) > 0:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            # 画像で下側が y 座標の大きい方に対応することに注意
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]: # y 座標の値で比較
                fingers.append(1)
            else:
                fingers.append(0)
        
        print(fingers)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), 
            cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    # print(fingers)
    sumFingers = fingers.count(1)
    cv2.putText(img, str(int(sumFingers)), (20, 70), 
            cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)




