

subdir=$1
tardir=$2

outdir=$3


while read pair
do

str=($pair)

echo $pair

sub=${str[0]}
tar=${str[1]}

echo $((sub))
echo ${tar} | bc

output=${outdir}"/"${sub}

#mkdir $output

#ln -s ${subdir}"/im"${sub}".nii.gz" ${output}"/"
#ln -s ${tardir}"/images/img_"${tar}".nii.gz" ${output}"/"
#ln -s ${tardir}"/annotations/mask_"${tar}".nii.gz" ${output}"/"

done < ready2reg.txt
