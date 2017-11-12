import numpy as np
# import cv2
# from skimage.transform import resize


def preprocessing(image: np.array) -> np.array:
    # gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    # gray = cv2.fastNlMeansDenoising(src=gray)
    return image

#
#
#
#

# # threshold
# thresh = None
# maxval = None
# thresh_type = None
# dst = None
#
# # adaptiveThreshold
# maxValue = None
# adaptiveMethod = None
# threshold_type = None
# blockSize = None
# C = None
# dst = None
#
# # Noisy removal
#
# dst = None
# anchor = None
# borderType = None
#
# # Erode and Dilate
#
# iter_erode = None
# iter_dilate = None
#
# #
# #
# #
# #
#
# image = np.zeros((500, 500))
#
#
# # What will be function?
#
# # binarisation
#
# threshold = cv2.threshold(src=image,
#                           thresh=thresh,
#                           maxval=maxval,
#                           type=thresh_type,
#                           dst=dst)
#
# adaptive_threshold = cv2.adaptiveThreshold(src=image,
#                                            maxValue=maxValue,
#                                            adaptiveMethod=adaptiveMethod,
#                                            thresholdType=threshold_type,
#                                            blockSize=blockSize,
#                                            C=C,
#                                            dst=dst)
#
# # Rescaling
#
# resize(image=image, output_shape=(500, 500))
#
# # Noise removal
#
# cv2.blur(src=image, ksize=(9, 9), dst=dst, anchor=anchor, borderType=borderType)
#
# # Morphology
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(3, 3))
# cv2.morphologyEx(src=image, op=cv2.MORPH_CLOSE, kernel=kernel)
#
# # Erode and Dilate
#
# cv2.erode(src=image, kernel=None, iterations=iter_erode)
# cv2.dilate(src=image, kernel=None, iterations=iter_dilate)
