import cv2
import os
def get_streams(f_movie):
    capture = cv2.VideoCapture(f_movie)
    fourcc = capture.get(cv2.CAP_PROP_FOURCC)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    frameSize = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                 int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    numframes = int(capture.get(7))

    for i in range(numframes):
        _, frame = capture.read()
        # convert the RGB image to gray
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # save each frame as jpg
        #cv2.imwrite("frame%d.jpg" % i, frame)
        path = os.getcwd()
        filename = 'frames'
        path = os.path.join(path, filename)
        cv2.imwrite(path +'/'+"frame%d.jpg" % i, frame)


    return capture

##########################################################################

get_streams('tumor_dual.avi')



