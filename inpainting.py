import numpy as np
import cv2

img = cv2.imread('test-2/a.png')     # input
mask = cv2.imread('test-2/b.png',0)  # mask

dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
dst_NS = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

cv2.imwrite('clean_telea_image.png', dst_TELEA)
cv2.imwrite('clean_ns_image.png', dst_NS)
