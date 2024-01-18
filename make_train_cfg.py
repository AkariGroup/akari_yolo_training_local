import yaml
import os

with open(
    os.path.dirname(os.path.abspath(__file__)) + "/data/akari_train_data.yaml"
) as file:
    obj = yaml.safe_load(file)
    nc = obj["nc"]

with open(
    os.path.dirname(os.path.abspath(__file__)) + "/yolov7/cfg/training/yolov7-tiny.yaml"
) as param_file:
    param = yaml.safe_load(param_file)
    param["nc"] = nc

with open(
    os.path.dirname(os.path.abspath(__file__)) + "/data/akari_train_cfg.yaml", "w"
) as file:
    yaml.dump(param, file, default_flow_style=True)
