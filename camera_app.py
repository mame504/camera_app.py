# -*- coding: utf-8 -*-

import cv2
import dlib
import numpy as np
from imutils import face_utils

face_landmark_path = './shape_predictor_68_face_landmarks.dat' #学習済みデータへのパス



def main():
    # return
    cap = cv2.VideoCapture(0) #カメラから画像を取得
    if not cap.isOpened():
        print("Unable to connect to camera.") #カメラが見つからないとき
        return
    

    detector = dlib.get_frontal_face_detector() 
    predictor = dlib.shape_predictor(face_landmark_path)

    img = cv2.imread('scr2.png')
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            face_rects = detector(frame, 0)

            if len(face_rects) > 0: #特徴点を取得できたとき
                shape = predictor(frame, face_rects[0]) #検出した器官をshapeに保存
                shape = face_utils.shape_to_np(shape) #shapeに保存したデータを扱いやすい形へ
                cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('screen', img)

            cv2.imshow("demo", frame)

            #qキーを押して終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    main()