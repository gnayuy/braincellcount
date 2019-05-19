
# imrot.py
# rotate image specified angle in a clockwise direction 
# Yang Yu, gnayuy@gmail.com

# Usage: 

#
import sys
import skimage
import nibabel as nib
import numpy as np
from PIL import Image
import nrrd
import math
#import imutils
import cv2

#
def rotate_bound(image, angle):
    (h,w) = image.shape[:2]
    (cx, cy) = (w//2, h//2)
    M = cv2.getRotationMatrix2D((cx,cy), angle, 1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])

    nW = int((h*sin) + (w*cos))
    nH = int((h*cos) + (w*sin))

    M[0,2] += (nW/2) - cx
    M[1,2] += (nH/2) - cy

    return cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_NEAREST)

#
inputImg = sys.argv[1]
outputImg = sys.argv[2]
angle = int(sys.argv[3])

# load
image = nib.load(inputImg)
img = image.get_fdata()

# rotate 90
#img = img.swapaxes(-2,-1)[...,::-1,:]

print(angle)

#rotated = imutils.rotate_bound(img, angle)
rotated = rotate_bound(img, angle)

# save
im = nib.Nifti1Image(rotated, np.eye(4))
im.to_filename(outputImg)


