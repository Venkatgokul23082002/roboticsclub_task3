#############################
# import necessary libraries
#############################
import cv2
import cv2.aruco
import matplotlib.pyplot as plt
import imutils
import numpy as np
from google.colab.patches import cv2_imshow
import time
import matplotlib
import os

####################################################################
def get_frame(time_sec):
    '''
    Reads the given video(aruco_bot.mp4) and captures the frame at the given second that is provided as the argument
    Parameters
        ----------
        time_sec : str
                time in seconds at which the frame is to be captured

    Returns
    -------
    frame : numpy array
        frame at the given second
    '''
    ##############	ADD YOUR CODE HERE	##############
time=input()
cap = cv2.VideoCapture('./aruco_bot.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) 
frame_seq = int(time)*fps
cap.set(1, frame_seq)
ret, frame = cap.read()  
cap.release()
    ##################################################
    frame = ''
    return frame


def detect_Aruco(frame):
    '''
    Reads the given frame and detects ArUco markers in it.
    Parameters
    ----------
    frame : numpy array
        frame in which ArUco markers are to be detected

    Returns
    -------
    corners : list
        list of corners of ArUco markers in the frame
    '''
    ##############	ADD YOUR CODE HERE	##############

alpha = float(2.2)
beta = int(45)
frame = np.clip(alpha*frame + beta, 0, 255)
gray=cv2.cvtColor(frame.astype('float32'),cv2.COLOR_BGR2GRAY)
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
arucoParams = cv2.aruco.DetectorParameters_create()
corners, ids, rejected = aruco.detectMarkers(gray.astype('uint8'), arucoDict, parameters = arucoParam)
    ##################################################
    corners = []
    return corners


def mark_Aruco(frame, corners):
    '''
    Draws a frame with detected ArUco markers in it that is mark the four corners of the aruco marker 
    and display the respective id of the marker.
    Parameters
    ----------
    frame : numpy array
        frame in which ArUco markers are to be marked
    corners : list
        list of corners of ArUco markers in the frame

    Returns
    -------
    marked_frame : numpy array
        frame with ArUco markers marked
    '''
    ##############	ADD YOUR CODE HERE	##############

x_sum = corners[0][0][0][0]+ corners[0][0][1][0]+ corners[0][0][2][0]+ corners[0][0][3][0]
y_sum = corners[0][0][0][1]+ corners[0][0][1][1]+ corners[0][0][2][1]+ corners[0][0][3][1]  
cX= x_sum*0.25
cY = y_sum*0.25
cv2.circle(frame, (int(cX),int( cY)), 4, (0, 0, 255), -1)
cv2.putText(frame, str(ids[0][0]),(int(cX)+3,int(cY)), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
for i in range(0,4):
  cv2.circle(frame, (corners[0][0][i][0],corners[0][0][i][1]), 4, (0, 0, 255), -1)
cv2_imshow(frame)
    ##################################################
    marked_frame = ''
    return marked_frame


############################################################################################
# main function
############################################################################################
if __name__ == '__main__':
    frame = get_frame(input("time value in seconds:"))
    corners = detect_Aruco(frame)
    marked_frame = mark_Aruco(frame, corners)
