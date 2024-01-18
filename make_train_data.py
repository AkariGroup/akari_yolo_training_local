import yaml
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/data/dataset"

f = open(DATA_DIR + "/classes.txt")
class_list = f.read().split("\n")
class_list = [a for a in class_list if a != ""]
data = {}
data["train"] = DATA_DIR + "/images/train"
data["val"] = DATA_DIR + "/images/valid"
data["test"] = DATA_DIR + "/images/test"

data["nc"] = len(class_list)
data["names"] = class_list
print(data)
with open(
    os.path.dirname(os.path.abspath(__file__)) + "/data/akari_train_data.yaml", "w"
) as file:
    yaml.dump(data, file)
