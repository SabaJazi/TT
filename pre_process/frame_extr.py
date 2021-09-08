import cv2

def get_streams(f_movie):
    capture = cv2.VideoCapture(f_movie)
    fourcc = capture.get(cv2.CAP_PROP_FOURCC)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    frameSize = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                 int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    numframes = capture.get(7)

    # out = cv2.VideoWriter('test_track.mp4',
    #                       cv2.VideoWriter_fourcc(*'MP4V'),
    #                       fps / 10,
    #                       frameSize)
    return capture

##########################################################################

capture= get_streams('tumor_dual.avi')
num_frames=int(capture.get(7))
print(num_frames)
for i in range(num_frames):
  _, frame = capture.read()
  #convert the RGB image to gray
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #save each frame as jpg
  cv2.imwrite("frame%d.jpg" % i, frame)


