#
# rotate3d.py
# rotate 3d image stack
# Usage: python rotate3d.py input3d.nrrd output3d.nrrd angle axis interpolation
# angle [0,360]
# axis: x/y/z
# interpolation: 0: nearest neighbor; 1: b-spline order=3 
# example: python rotate3d.py ccf_img.nrrd ccf_imgrot.nrrd 10 z 1
# Yang Yu (gnayuy@gmail.com)
#

import sys
import numpy as np
import nrrd
from scipy import ndimage

#
inputImg = sys.argv[1]
outputImg = sys.argv[2]
angle = float(sys.argv[3])
axis = sys.argv[4]
interp = int(sys.argv[5])

#
data, header = nrrd.read(inputImg)

rot_axis = np.argmin(data.shape)

if data.ndim < 3:
    raise RuntimeError('Input is not 3 dimensions!')

if interp == 1:
    bsorder = 3
elif interp == 0:
    bsorder = 0
else:
    raise RuntimeError('Invalid interpolation method!')

if axis == 'x':
    imrot = ndimage.rotate(data, angle, axes=((rot_axis+1)%3, (rot_axis+2)%3), order=bsorder, reshape=True )
elif axis == 'y':
    imrot = ndimage.rotate(data, angle, axes=((rot_axis+2)%3, (rot_axis+3)%3), order=bsorder, reshape=True )
elif axis == 'z':
    imrot = ndimage.rotate(data, angle, axes=((rot_axis+1)%3, (rot_axis+3)%3), order=bsorder, reshape=True )
else:
    raise RuntimeError('Invalid axis!')

nrrd.write(outputImg, imrot)


