time for((i=1001; i<1005; i++)); do python analysis.py binary/${i}.tif warp_mask/${i}/cc_warpedmask.nii.gz fig${i}.eps; done
