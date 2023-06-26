import os
import random
import shutil

##          Joe, 22-06-2023
#
# After using yolo_label, you will get a bunch of images with annotations.
# This python file will seperate the images and annotations into yolo format
# Into 'Train/Valid/Test' so that we can immediately start to do training
#
##

# Set the path to the folder containing images and annotations
data_folder = "./"

# Set the path to the output folders
train_folder = "./train"
val_folder = "./valid"
test_folder = "./test"

# Set the split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# =========================

# Create the output folders if they don't exist
os.makedirs(os.path.join(train_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(train_folder, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(val_folder, "labels"), exist_ok=True)
os.makedirs(os.path.join(test_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(test_folder, "labels"), exist_ok=True)

# Get the list of all files in the data folder
all_files = os.listdir(data_folder)

# Filter and get the list of image files
image_files = [filename for filename in all_files if filename.endswith(".jpg")]

# Filter and get the list of annotation files
annotation_files = [filename for filename in all_files if filename.endswith(".txt")]

# Shuffle the image files
random.shuffle(image_files)

# Calculate the number of images for each split
num_images = len(image_files)
num_train = int(num_images * train_ratio)
num_val = int(num_images * val_ratio)
num_test = num_images - num_train - num_val

# Split the image files into train, val, and test sets
train_files = image_files[:num_train]
val_files = image_files[num_train:num_train + num_val]
test_files = image_files[num_train + num_val:]

# Move the image files to the corresponding output folders
for file in train_files:
    image_path = os.path.join(data_folder, file)
    annotation_path = os.path.join(data_folder, file.replace(".jpg", ".txt"))
    shutil.move(image_path, os.path.join(train_folder, "images", file))
    shutil.move(annotation_path, os.path.join(train_folder, "labels", file.replace(".jpg", ".txt")))

for file in val_files:
    image_path = os.path.join(data_folder, file)
    annotation_path = os.path.join(data_folder, file.replace(".jpg", ".txt"))
    shutil.move(image_path, os.path.join(val_folder, "images", file))
    shutil.move(annotation_path, os.path.join(val_folder, "labels", file.replace(".jpg", ".txt")))

for file in test_files:
    image_path = os.path.join(data_folder, file)
    annotation_path = os.path.join(data_folder, file.replace(".jpg", ".txt"))
    shutil.move(image_path, os.path.join(test_folder, "images", file))
    shutil.move(annotation_path, os.path.join(test_folder, "labels", file.replace(".jpg", ".txt")))

print("Data splitting completed.")