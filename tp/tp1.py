import numpy as np
import cv2
import glob
#%matplotlib inline

# Object coordinates
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store image points.
imgp = [] # 2d points in image plane.


# Read image
img = cv2.imread('left1.jpg')

# Command #1 
# change the color of image from RGB to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Command #2  
# Find the inner corner position of the board map gray
# (7,6) : The number of corners per line and column in the board map
# Output : the number of corner points
# ret = TRUE
ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

# Termination criteria for Command 3
# TERM_CRITERIA_EPS : Accuracy (error) meets epsilon stop
# TERM_CRITERIA_MAX_ITER : The number of iterations exceeds max_iter to stop
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Command #3
# cornerSubPix : Accurate corner position in corner detection
# (11,11) : Half of the length of the search window
# (-1,-1) : Half of the length of the dead region in the middle of the search area,  If the value is set to (-1, -1), there is no such area.
# criteria : Termination of the corner point precision iterative process
cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
imgp.append(corners)

# Command #4
# Chessboard corner drawing
cv2.drawChessboardCorners(img, (7,6), corners,ret)

# Image display with its points
cv2.namedWindow('Test calibration')
cv2.startWindowThread()
cv2.imshow('Test calibration',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objp, imgp, gray.shape[::-1],None,None)

