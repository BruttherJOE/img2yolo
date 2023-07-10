# img2yolo Instructions

This repository provides instructions on how to convert collected images into the YOLO format and perform train/test/valid split.

## YOLO Labeling Tool

The repository includes a cloned version of Yolo_Label, which is a labeling tool used to annotate images. Please note that this tool is not developed by me, but it is included here to ensure version compatibility. [cr https://github.com/developer0hye/Yolo_Label]   

**Note:** Yolo_Label can only be used in Windows. If you are using Ubuntu version 22.04 or higher, refer to the provided link for alternative instructions.

## Label Images

1. Use Yolo_Label to annotate your images. This tool allows you to label objects of interest in your images.

2. After using Yolo_Label, you will obtain a set of labeled images. Place all the labeled images in a single folder.

## Train/Test/Valid Split

To perform the train/test/valid split of your labeled images, follow these steps:

1. Run the `yolo_slice_sort_windows.py` Python script provided in this repository. This script is designed to slice the images into the train, test, and valid sets according to specified ratios. Adjust the ratios as necessary in the Python file.

   **Note:** This script has been tested on windows. If you are using linux, you may need to modify the folder paths accordingly. There is an old version of the script that I had written for linux, however it does not print out what it is doing and the user may need to debug. MAKE SURE ALL THE FILE EXTENSIONS ARE CORRECT!

2. The script will generate separate folders for the train, test, and valid sets, containing the sliced images.

## Training the Images

To train the images using YOLO, follow the standard procedures for training a YOLO model. This repository focuses on the initial steps of data preparation and does not provide detailed instructions for training the model.

The folder hierarchy should now look like this :
```
fasteners/
├─── test/
│      ├─── images/
│      ├─── labels/
├─── train/
│      ├─── images/
│      ├─── labels/
├─── valid/
│      ├─── images/
│      ├─── labels/
├─── labels.txt
├─── fasteners.yaml

```

## Labels.txt

Add your classes into the labels.txt file, one class per line. For example,
```
nut
bolt
```

## .yaml file

This can be renamed to <your_name_here>.yaml. The structure of this file could be as follows (for YOLOv8)
```
train: ./train/images
val: ./valid/images
test: ./test/images

nc: 2
names: ['nut', 'bolt']
```

nc stands for number of classes, in this case 1. 
names are the names of classes.

you do not really need to change where the image is saved, it should be as above.
