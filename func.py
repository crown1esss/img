import cv2 as cv
import numpy as np


def canny(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    blur = cv.GaussianBlur(img, (5, 5), 0)
    return cv.Canny(blur, 50, 150)
