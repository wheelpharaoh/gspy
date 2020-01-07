import os

import yaml

cfg = {}


dir_path = os.path.dirname(os.path.realpath(__file__))
config_yaml = os.path.join(dir_path, './config.yaml')

with open(config_yaml, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
