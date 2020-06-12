
#

# set ANTs program environment path
# export PATH=~/work/tools/ANTs/build/bin:$PATH

# alias python=python3

while read line
do

str=($line)

numdir=${str[0]}
rot=${str[1]}

output=${numdir}"/cc"

skip=${numdir}"/cc_3drec.nii.gz"

if [ -f $skip ]
then

continue;

fi


# echo ${str[0]} ${str[1]}

while read file
do

if [[ $file =~ ${numdir} ]]
then

str=($file)

ccfimg=${str[0]}
ccfmsk=${str[1]}
brain=${str[2]}

break;

fi

done < files.txt

if [[ ${rot} > 0 ]]
then

tmp=${ccfimg}
ccfimg=${tmp%*.nii.gz}rot.nii.gz

time python imrot.py $tmp $ccfimg $rot

tmp=${ccfmsk}
ccfmsk=${tmp%*.nii.gz}rot.nii.gz

time python imrot.py $tmp $ccfmsk $rot

echo " ${ccfimg} ${ccfmsk} ${brain} rotate $rot"

else

echo "${ccfimg} ${ccfmsk} ${brain} no rotations"

fi

echo "run ... ${ccfimg} ${ccfmsk} ${brain}"

time python reg.py ${ccfimg} ${ccfmsk} ${brain} ${output}

if [[ ${rot} > 0 ]]
then

time python imrot.py $skip $skip $((360 - rot))

else

echo "${ccfimg} ${ccfmsk} ${brain}"

fi


done < rotations.txt

