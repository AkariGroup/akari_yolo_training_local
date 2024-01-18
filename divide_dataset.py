import glob
import shutil
import random
import os

# 学習データの割合(Percentage of training data)
train_ratio = 0.8
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/images"
TRAIN_DIR = DATA_DIR + "/train"
TEST_DIR = DATA_DIR + "/test"

dataset_directory = os.path.dirname(os.path.abspath(__file__)) + "/data/dataset"
train_images_directory = dataset_directory + "/images/train"
train_labels_directory = dataset_directory + "/labels/train"
valid_images_directory = dataset_directory + "/images/valid"
valid_labels_directory = dataset_directory + "/labels/valid"
test_images_directory = dataset_directory + "/images/test"

os.makedirs(train_images_directory, exist_ok=True)
os.makedirs(train_labels_directory, exist_ok=True)
os.makedirs(valid_images_directory, exist_ok=True)
os.makedirs(valid_labels_directory, exist_ok=True)

class_file = TRAIN_DIR + "/classes.txt"
shutil.copy2(class_file,dataset_directory)
# コピー元ファイルリスト取得(Get copy source file list)
annotation_list = sorted(glob.glob(TRAIN_DIR + "/*.txt"))
image_list = sorted(glob.glob(TRAIN_DIR + "/*.jpg"))


file_num = len(annotation_list)
# インデックスシャッフル(shuffle)
index_list = list(range(file_num - 1))
random.shuffle(index_list)

for count, index in enumerate(index_list):
    if count < int(file_num * train_ratio):
        # 学習用データ(Training Data)
        shutil.copy2(annotation_list[index], train_labels_directory)
        shutil.copy2(image_list[index], train_images_directory)
    else:
        # 検証用データ(Validation Data)
        shutil.copy2(annotation_list[index], valid_labels_directory)
        shutil.copy2(image_list[index], valid_images_directory)


shutil.copytree(TEST_DIR, test_images_directory)
