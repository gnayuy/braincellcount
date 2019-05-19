

### step 0. collect pairs of images for registration

# time n=1000; while read file; do echo "process $file ..."; if [ -f $file ]; then n=$((n+1)); echo $file;  python zeroBoundary_hsv6.py $file sampled/im${n}.nii.gz; fi; done < filelist.txt

# sh pairImages.sh ${PWD}/sampled ${PWD}/../ccf reg

### step 1. pairwise registration

cd reg

# time python imrot180_hsv6.py 1001/img_447.nii.gz 1001/img_447rot.nii.gz 
# time python imrot180_hsv6.py 1001/mask_447.nii.gz 1001/mask_447rot.nii.gz 
# time python reg.py 1001/img_447rot.nii.gz 1001/mask_447rot.nii.gz 1001/im1001.nii.gz 1001/cc

# time python reg.py 1002/img_462.nii.gz 1002/mask_462.nii.gz 1002/im1002.nii.gz 1002/cc

# time python imrot180_hsv6.py 1003/mask_477.nii.gz 1003/mask_477rot.nii.gz 
# time python imrot180_hsv6.py 1003/img_477.nii.gz 1003/img_477rot.nii.gz 
# time python reg.py 1003/img_477rot.nii.gz 1003/mask_477rot.nii.gz 1003/im1003.nii.gz 1003/cc


time sh batchprocess.sh

for i in  */*rec*; do n=${i%*/*}; file=${i#*/*}; cp $i ${file%*.nii.gz}$n".nii.gz"; done

mkdir eval

mv cc_3drec10* eval


