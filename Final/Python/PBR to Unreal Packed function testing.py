'''----------------------------------------- PBR to Unreal Packed functionality -----------------------------------------'''

# importing necessary packages
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

#allow openCV to read .exr files: (may not be used due to it needing more conversions)

os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"

# For ease of testing:

imgPath = "H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\Final\Asset\Testing PBR to AOR"

# load images to combine:

MetallicImg = cv2.imread( imgPath + "rust_coarse_01_ao_2k" , cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

OcclusionImg = cv2.imread( imgPath + "rust_coarse_01_ao_2k" , cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

RoughnessImg = cv2.imread( imgPath + "rust_coarse_01_rough_2k" , cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

# Separate each image into the channel it will fill




