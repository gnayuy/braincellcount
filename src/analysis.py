

# statistics of cells in standard mouse brain compartment
# yang yu, gnayuy@gmail.com

# put the standard brains compartment csv file and your interested compartments csv file in the folder
# Usage: python analysis.py cellseg.tif alignedannotations.nii.gz fig.eps
# example: python analysis.py binaryimage/1_1_Object Predictions.tif reg/1001/cc_warpedmask.nii.gz fig1.eps

#
import sys
import numpy as np
import skimage
import nibabel as nib
from PIL import Image
import pandas
import matplotlib.pyplot as plt

#
binimg = sys.argv[1]
warpedmask = sys.argv[2]
outfig = sys.argv[3]

# annotations
annotations='annotations4index.csv'
selected='interestedregions.csv'

anno = pandas.read_csv(annotations, names=['Acronym', 'ID', 'Color'])
interested = pandas.read_csv(selected)
rois = interested.loc[:,"Acronym"]

# cell counts
im = skimage.io.imread(binimg, plugin='tifffile');

mask = nib.load(warpedmask)
m = mask.get_fdata()
umask = skimage.transform.rescale(m, 8, order=0)

# resize to the binary image
nsize = im.shape
osize = umask.shape

pos = (nsize[1] - osize[1])/2, (nsize[0] - osize[0])/2
posint = np.array(pos, dtype='int')

urm = Image.new('I', (nsize[1],nsize[0]))
urm.paste(Image.fromarray(umask), (posint[0], posint[1]) ) # [left, upper, right, lower]

umint = np.asarray(urm)

# statistics
n = rois.size

x = np.array(['aaaaaa' for _ in range(n)])
y = np.array([0 for _ in range(n)])

for i in range(n):
    #print(rois.iloc[i])
    
    x[i] = rois.iloc[i]
    
    [idx] = anno[anno.Acronym==rois.iloc[i]].index.values
    color = anno.iloc[idx, 2]
    
    result = anno[anno.Color==color]
    
    #print(result.size)
    
    array = result.iloc[:,1].to_numpy()
    a = array.astype('int')
    
    maskImage = np.where(umint==a[0], im, 0)
    
    n = a.size
    
    if(n>1):
        for j in range(1, n):
            maskImage = np.add(maskImage, np.where(umint==a[j], im, 0))

    labeledImage = skimage.measure.label(maskImage)
    #print(i, np.max(labeledImage), labeledImage.shape)
    y[i] = np.max(labeledImage)

# plot
xx = np.arange(0,rois.size)

plt.xlabel('Mouse Brain Area of Interests')
plt.ylabel('Cell Counts')
plt.title('Cells in ROIs')

plt.bar(xx, y, align='center', alpha=0.5)
plt.xticks(xx, x, rotation='vertical')
plt.margins(0.01)
plt.subplots_adjust(bottom=0.15)
plt.xticks(fontsize=4, rotation=90)
plt.savefig(outfig, format='eps')
#plt.show()
