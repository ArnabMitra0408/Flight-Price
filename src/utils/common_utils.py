import yaml
import os
import pandas
import logging
import shutil


def read_params(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    logging.info(f"read parameters")
    return config

def clean_dir(dir_path:str) -> None:
    if len(os.listdir(dir_path)) == 0:
        print(f'directory {dir_path} already empty')
    else:
        shutil.rmtree(dir_path)
        print('directory emptied')

def create_dir(paths:list) -> None:
    for path in paths:
        if os.path.exists(path):
            print(f'directory {path} already exists')
        else:
            os.mkdir(path)
            print(f'directory {path} created')

def save_data(data,path:str):
    try:
        data.to_csv(path,index=False)
        print('data saved')
    except:
        print('Data could not be saved')