import cv2
import os

img_array = []
main_path = os.getcwd()
filename = 's&p_noisy'
path = os.path.join(main_path, filename)
#----------------------------------------------

for image in os.listdir(path):

    image_path = os.path.join(path, image)
    frame = cv2.imread(image_path)
    #print(image_path)
    raw_image = cv2.imread(image_path)

    height, width, layers= raw_image.shape
    size = (width, height)
    img_array.append(raw_image)

out = cv2.VideoWriter('s&p_noisy.mp4',cv2.VideoWriter_fourcc(*'mp4v'),
                        8, size)
for i in range(len(img_array)):
    out.write(img_array[i])

    if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
        break
out.release()
