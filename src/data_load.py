import pandas as pd
import logging
import os
import shutil
from argparse import ArgumentParser
import yaml
from utils.common_utils import read_params,clean_dir,create_dir,save_data

def load_data(data_path:str,directory_path:str,local_data_save_path:str,main_data_folder_path:str) -> None:
    #clean data directory

    clean_dir(main_data_folder_path)
    #create_dir

    create_dir([main_data_folder_path,directory_path])
    #load data
    
    file_id=data_path.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id+'&export=download'
    data = pd.read_csv(dwn_url)

    #save data csv in desired location

    save_data(data,local_data_save_path)

if __name__ == '__main__':
    args=ArgumentParser()
    args.add_argument('--config_file_path',default='params.yaml')
    parsed_args=args.parse_args()
    
    configs=read_params(parsed_args.config_file_path)
    main_data_folder_path=configs['artifacts']['artifacts_dir']
    directory_path=configs['artifacts']['raw_local_data_dir']
    data_path=configs['data']['gdrive']
    local_data_save_path=configs['artifacts']['raw_local_data']
    
    try:
        load_data(data_path,directory_path,local_data_save_path,main_data_folder_path)
    except Exception as e:
        raise e
    