#
# setup python environment
# pip install --upgrade pip, scikit-image, numpy, Pillow, nibabel
#
# This is the first preprocessing step: downsample and resize all images into the same size
#
# Usage:
#
# for i in {1..15}_{1..10}.tif; do echo $i >> filelist.txt; done
# n=100; while read file; do if [ -f $file ]; then n=$((n+1)); python zeroBoundary_hsv6.py $file im${n}.nii.gz; fi; done < filelist.txt

import sys
import skimage
import nibabel as nib
import numpy as np
from PIL import Image
import nrrd

#
inputImg = sys.argv[1]
outputImg = sys.argv[2]

#
im = skimage.io.imread(inputImg, plugin='tifffile');

imds = skimage.transform.downscale_local_mean(im[:,:,0], (8,8)) # 8x

imdsint = np.array(imds, dtype='uint16')

img = imdsint;
img[0,:] = 0;
img[-1,:] = 0;
img[:,0] = 0;
img[:,-1] = 0;

# save
im = nib.Nifti1Image(img, np.eye(4))
im.to_filename(outputImg)
