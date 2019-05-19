

n=0; while read line; do str=($line) erased[$n]=${str[1]}; n=$((n+1)); done < ../../ready2reg.txt


n=1001;

for e in ${erased[@]}
do

fn="warped/cc_3drec"${n}".nii"

n=$((n+1))

m=$((e+1000))
filename="im"${m}".nii"


ln -s $fn $filename

done





for((i=1; i<=1320; i++))
do

arr[$i]=$i

done

links=(${arr[@]/$erased})

# echo ${links[@]}

for e in ${links[@]}
do

n=$((e + 1000))

filename="im"${n}".nii"

ln -s ../zero.nii $filename

done

