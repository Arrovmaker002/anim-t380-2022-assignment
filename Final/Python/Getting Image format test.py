'''----------------------------------------- PBR to Unreal Packed functionality -----------------------------------------'''
# importing necessary packages
import os
import numpy as np
import pathlib
from PIL import Image
from PIL.ExifTags import TAGS
import cv2


#imagename = input('image file path: ')

# read the image data using PIL and set the image data to variable "image"
Testimage = Image.open(r'C:\Users\vince\Downloads/Test_Opencv2')

# extract the format from the metadata
# extracting the exif metadata
exifdata = Testimage.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")

