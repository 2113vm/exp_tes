import cv2


def preprocessing(image):
    gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    gray = cv2.fastNlMeansDenoising(src=gray)
    return gray
