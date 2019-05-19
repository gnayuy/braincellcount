

# python reg.py ccfimg ccfano image output

import sys
import skimage
import nibabel as nib
import numpy as np
from PIL import Image
import nrrd
import subprocess
import os

#
inputImg = sys.argv[1]
inputMsk = sys.argv[2]
brainImg = sys.argv[3]
output = sys.argv[4]

# 

print(inputImg, brainImg)

#
command = 'time ANTS 2 -m MI[ ' + brainImg + ', ' + inputImg + ', 1, 128] -o ' + output + ' -i 0 --use-Histogram-Matching --number-of-affine-iterations 10000x10000x10000x10000' 


print(command)
#subprocess.run([ command ])
os.system( command )


affinematrix = output + 'Affine.txt'

affinewarpedimage = output + '_affine.nii.gz'
warpedimage = output + '_warped.nii.gz'
warpedmask = output + '_warpedmask.nii.gz'

command = 'time WarpImageMultiTransform 2 ' + inputImg + ' ' + affinewarpedimage + ' -R ' + brainImg + ' ' + affinematrix

print(command)
#subprocess.run([ command ])
os.system(command)


out = output + 'ccmi'
aff = out + 'Affine.txt'
fwd = out + 'Warp.nii.gz'
bwd = out + 'InverseWarp.nii.gz'

command = 'time ANTS 2 -m CC[ ' + brainImg + ', ' + inputImg + ', 0.25, 8] -m MI[ ' + brainImg + ', ' + inputImg + ', 0.75, 128] -t SyN[0.25] -r Gauss[3,0] -o ' + out + ' -i 500x250x125 --initial-affine ' + affinematrix
#command = 'time ANTS 2 -m MI[ ' + brainImg + ', ' + inputImg + ', 1, 128] -t SyN[0.2] -r Gauss[2,0] -o ' + out + ' -i 1000x500x250x125 --initial-affine ' + affinematrix
print(command)
os.system(command)

# result
command = 'time WarpImageMultiTransform 2 ' + inputMsk + ' ' + warpedmask + ' -R ' + brainImg + ' ' + fwd + ' ' + aff + ' --use-NN'
print(command)
os.system(command)

# secondary results for evaluation and visualization
command = 'time WarpImageMultiTransform 2 ' + inputImg + ' ' + warpedimage + ' -R ' + brainImg + ' ' + fwd + ' ' + aff
print(command)
os.system(command)

invwarped = output + '_3drec.nii.gz'

command = 'time WarpImageMultiTransform 2 ' + brainImg + ' ' + invwarped + ' -R ' + inputImg + ' -i ' + aff + ' ' + bwd
print(command)
os.system(command)

