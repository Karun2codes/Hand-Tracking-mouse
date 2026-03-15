import cv2 as cv
import mediapipe as mp
import pyautogui
import math

mp_hands = mp.solutions.hands
drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)

screen_Width, screen_Height = pyautogui.size()
pinch_start =30

cam = cv.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

palmid = [0,5,9,13,17]   
dead_zone = 16
prev_x, prev_y = screen_Width//2, screen_Height//2

    
while True:
    success, frame = cam.read()
    if not success:
        print("no camera found")
        break
            
    frame = cv.flip(frame, 1)
    h,w,_= frame.shape
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    detected = hands.process(frameRGB)

    if detected.multi_hand_landmarks:
        for landmarks in detected.multi_hand_landmarks:
                # print(landmarks)
                # drawing.draw_landmarks(
                #     image=frame,
                #     landmark_list=landmarks,
                #     connections=mp_hands.HAND_CONNECTIONS
                # )
                index_tip = landmarks.landmark[8]
                thumb_tip = landmarks.landmark[4]

                cx = sum(landmarks.landmark[id].x for id in palmid) / len(palmid)
                cy = sum(landmarks.landmark[id].y for id in palmid)
                screen_x = int(cx * screen_Width)
                screen_y = int(cy * screen_Height)
                dx = screen_x - prev_x
                dy = screen_y - prev_y
                if math.hypot(dx,dy) > dead_zone:
                    pyautogui.moveTo(screen_x,screen_y,duration=0)
                    prev_x = screen_x
                    prev_y = screen_y
                ix,iy = int(index_tip.x * w),int(index_tip.y * h)
                tx,ty = int(thumb_tip.x * w),int(thumb_tip.y * h)

                pinch_distance = math.hypot(ix-tx , iy-ty)

                if pinch_distance < pinch_start:
                    pyautogui.click()

    cv.imshow("Hand Landmark", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()