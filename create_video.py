import cv2
import os
import re


# ----------------sorting the frame numbers ---------------------


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]


# #############################################


def create_video(path,name):
    images = [img for img in os.listdir(path)]
    sorted_images = sorted(images, key=natural_sort_key)
    img_array = []
    for image in sorted_images:
        image_path = os.path.join(path, image)
        raw_image = cv2.imread(image_path)
        height, width, layers = raw_image.shape
        size = (width, height)
        img_array.append(raw_image)
    video_name = name+'.mp4'
    # it writes the video in the main path, fix it later
    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'),
                          8, size)
    for i in range(len(img_array)):
        out.write(img_array[i])

        if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
            break
    out.release()

# ---------------------------------------------


main_path = os.getcwd()
folder_name = 's&p_0.01'
path = os.path.join(main_path, folder_name)
create_video(path, "s&p_0.01")