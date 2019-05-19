

# imrec.py to resize the size of the image A to the size of image B
#

import sys
import numpy as np
import nibabel as nib
from PIL import Image

#
imA = sys.argv[1]
imB = sys.argv[2]
imOut = sys.argv[3]

#

imga = nib.load(imA)
a = imga.get_fdata()

imgb = nib.load(imB)
b = imgb.get_fdata()

#
nsize = b.shape
osize = a.shape

pos = (nsize[1] - osize[1])/2, (nsize[0] - osize[0])/2 
posint = np.array(pos, dtype='int')

na = Image.new('F', (nsize[1], nsize[0]))
na.paste(Image.fromarray(a), (posint[0], posint[1]))


#
im = nib.Nifti1Image(np.asarray(na), np.eye(4))
im.to_filename(imOut)
