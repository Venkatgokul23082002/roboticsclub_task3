#############################
# import necessary libraries
#############################


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
