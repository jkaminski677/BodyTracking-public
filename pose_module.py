import cv2
import mediapipe as mp
import time
from datetime import datetime


class poseDetector():

    def __init__(self, mode = False, modComplex = 1, smoothLand = True, enSeg = False, smoothSeg = True, detection = 0.5, trackCon = 0.5):

        self.mode = mode
        self.modComplex = modComplex
        self.smoothLand = smoothLand
        self.enSeg = enSeg
        self.smoothSeg = smoothSeg
        self.detection = detection
        self.trackCon = trackCon


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.modComplex, self.smoothLand, self.enSeg,
                                self.smoothSeg, self.detection, self.trackCon)

    def findPose(self, img, draw = True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw = True):
        currentTime = datetime.now().strftime("%y-%m-%d %H:%M:%S.%f")[:-4]
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy, currentTime])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return lmList



def main():
    # cap = cv2.VideoCapture('PoseVideos/videoplayback.mp4')
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw = False)
        # print(lmList[20])
        cv2.circle(img, (lmList[20][1], lmList[20][2]), 15, (0, 0, 255), cv2.FILLED)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)),(79,50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Video", img)
        if cv2.waitKey(13) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()