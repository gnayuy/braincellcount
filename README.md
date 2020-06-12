BrainCellCount
===========

BrainCellCount is an open-source, semi-automatically Slice-to-volume Brain Aligner, to count cells via mapping mouse brain regions of interests (ROIs) between the studying brain and the CCFv3 (https://doi.org/10.1016/j.cell.2020.04.007).

Install
-------

BrainCellCount requires [ANTs registration toolkit](https://github.com/ANTsX/ANTs) to be installed.

BrainCellCount uses Python 3 and depends on python packages such as [numpy, scipy, scikit-image, ...](requirements.txt).

To create a new conda environment:

```
    conda create -n braincellcount python=3.8
    conda activate braincellcount
```
 
 Install required python packages:
 
 ```
    pip install -r requirements.txt
 ```
 
Get Started
--------------
 
 Here is a basic guide that introduces BrainCellCount and its functionalities.
 
* Data preparation

  * put your 2D slice images (*.tif) into a file "filelist.txt":
    `for i in {1..15}_{1..10}.tif; do echo $i >> filelist.txt; done`
  * downsample all images into the same size and set image boundaries with zeros:
    `n=100; while read file; do if [ -f $file ]; then n=$((n+1)); python zeroBoundary_hsv6.py $file im${n}.nii.gz; fi; done < filelist.txt`

* Map 2D slice images to CCFv3

  * select ~10 - 15 "key" 2D slice images and find matched the slice of CCFv3, save to "npoints.txt"
  * map the rest 2D slice images to CCFv3 using scipy.optimize.curve_fit, save all best matched pair images' z positions to "ready2reg.txt"
  * ensure to be registered the images are under "./sampled" and template images are under "./ccf", create an output folder ".reg"
  * proofread and label the slices when their rotations are more than 90 degrees to "rotations.txt" with 90/180/270, run:
    `sh batchprocess.sh`

* Count cells in each interested brain area
  * put cell segmentation images into "binaryimage" folder
  * put your ROIs into a CSV file "interestedregions.csv", e.g. [ROIs](src/interestedregions.csv) in this study
  * to obtain the cell counting result, run:
    `python analysis.py cellseg.tif alignedannotations.nii.gz fig.eps`

Citation
---------

To cite this software package, please reference, as appropriate:

> Rong Gong , Shengjin Xu, Ann Hermundstad , Yang Yu, Scott M. Sternson. Double negative feedback controls palatability in convergent hunger and thirst circuits. Cell. 2020.
