import os

main_path = os.getcwd()
filename = 'frames'
path = os.path.join(main_path, filename)
test_img = path+'\\'+'frame0.jpg'
print(test_img)