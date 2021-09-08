import os
# print(os.getcwd())
# print(__file__)
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")
#
# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")
#
# print("This file directory only")
# print(os.path.dirname(full_path))

path, filename = os.path.split(os.getcwd())
path=os.getcwd()
filename='frames'
path=os.path.join(path, filename).absolute()
#ospath+"frame%d.jpg" % i, frame
print(path)