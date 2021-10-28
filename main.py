import cv2 as cv
import func
import numpy
from object_detection import ObjectDetection
od = ObjectDetection()
def openf(name):
    video = cv.VideoCapture(name)
    if not video.isOpened():
        print('error')

    cv.waitKey(1)
    while video.isOpened():
        ret,frame = video.read()
        # frame = func.canny(frame)
        if not ret:
            break
        (class_ids , scores , boxes) = od.detect(frame)
        for box in boxes:
            (x,y,w,h) = box
            cv.rectangle(frame,(x,y),(x+w ,y+h) ,(0,255,0),2)


        cv.imshow('video',frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            video.release()
            cv.destroyAllWindows()
    video.release()
    cv.destroyAllWindows()

def main():
    name = 'data/test.mp4'
    openf(name)


if __name__ == '__main__':
    main()