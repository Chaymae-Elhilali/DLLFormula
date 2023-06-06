import cv2
import numpy as np

 
# read the image we want to work on and its directory
image = cv2.imread('image_1.jpg')  #attention PATH

# convert the image to grayscale format
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY) 

cv2.imwrite('image_thres.jpg', thresh)

# histogram stretching
min_intensity = np.min(thresh)
max_intensity = np.max(thresh)
stretched = (thresh - min_intensity) * (255 / (max_intensity - min_intensity))

# convert back to uint8
stretched = stretched.astype(np.uint8)

# save the stretched image
cv2.imwrite('stretched.jpg', stretched)
# ----------------------------------- erosion and dilation of images-------------------------------

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(stretched, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

#cv2.imshow('Input', image)
#cv2.imshow('Erosion', img_erosion)
#cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.imwrite('eroded_image.jpg', img_erosion)
cv2.imwrite('dilated_image.jpg', img_dilation)


# ------------------------------contours-------------------------------------------------

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
# since findContours alters the image
contours, hierarchy = cv2.findContours(image=img_dilation, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
# draw contours on the original image
image_copy = img_dilation.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# see the results

cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()