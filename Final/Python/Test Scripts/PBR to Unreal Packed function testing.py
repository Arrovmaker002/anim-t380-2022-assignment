'''----------------------------------------- PBR to Unreal Packed functionality -----------------------------------------'''

# importing necessary packages
import os
import numpy as np
import pathlib
from PIL import Image
from PIL.ExifTags import TAGS
import cv2

# Allow openCV to read .exr files: (may not be used due to it needing more conversions)

os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"

# image opening testing:

filePath = input('image file path: ') 
ext = pathlib.Path(filePath).suffix

print('the file extension is:'+ ext)
# load images to combine:

MetallicImg = cv2.imread(filePath + ext ,cv2.IMREAD_COLOR)

blue, green, red = cv2.split(MetallicImg)
  
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)

'''
cv2.destroyAllWindows()#OcclusionImg = cv2.imread( imgPath + "rust_coarse_01_ao_2k" , cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

#RoughnessImg = cv2.imread( imgPath + "rust_coarse_01_rough_2k" , cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

# Separate each image into the channel it will fill

#Metallic goes to the B channel (splitting all 3 and only going to keep one channel)

(blue, green, red) = cv2.split('mettalic', MetallicImg)

cv2.imshow('blue', blue)
cv2.waitKey(5)






# merging into final image

ArmImg = cv2.merge([MetallicImg, OcclusionImg, RoughnessImg])
'''