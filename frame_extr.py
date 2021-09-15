import cv2
import os
def get_streams(f_movie):
    capture = cv2.VideoCapture(f_movie)
    fourcc = capture.get(cv2.CAP_PROP_FOURCC)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    print('fps =' , fps)
    print('fourcc=', fourcc)
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
        cv2.imwrite(path +'/'+"%d.jpg" % i, frame)


    return capture

##########################################################################
# def get_streams2(video):
#
#     #vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
#     vidcap = cv2.VideoCapture(video)
#
#     success,image = vidcap.read()
#     count = 0
#     while success:
#       cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#       success,image = vidcap.read()
#       print('Read a new frame: ', success)
#       count += 1
# ##########################################################################
get_streams('tumor_dual.avi')



