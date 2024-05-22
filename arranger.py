import json
import os
import shutil
from pathlib import Path
from datetime import datetime
from file_types import FILE_TYPES

class Arranger:
    
    def __init__(self, home):
        self.home = home
        self.dir_dict = FILE_TYPES  
        self.config()
        self.logs = []

    def config(self):
        if not self.home == '':
            return
        
        self.current_path = os.path.dirname(__file__)
        config_path = str(Path.home()) + '/.config/arranger'
        Path(config_path).mkdir(exist_ok=True, parents=True)

        if not os.path.isfile(config_path + '/config.json'):
            shutil.copy(self.current_path + '/config.json', config_path + '/config.json')
        dictionary = {"path":str(Path.home())}
        with open('config.json', 'w') as conf:
            json.dump(dictionary, conf)
        with open(config_path + '/config.json', 'w') as outfile:
            json.dump(dictionary, outfile)
        self.home = Path.home()

    def verify(self):
        if os.path.exists(self.home):
            for directories in self.dir_dict.keys():
                if os.path.exists(f'{self.home}/{directories}'):
                    continue
                else:
                    os.mkdir(f'{self.home}/{directories}')
        else:
            quit(f'"{self.home}" directory does not exist.')

    def get_files(self):
        self.lst_of_paths = []
        self.lst_of_paths_home = []
        path_to_home = f'{self.home}'

        for directories in self.dir_dict.keys():
            path_to_file = f'{self.home}/{directories}'    
            for filename in os.listdir(path_to_file):
                self.f = os.path.join(path_to_file, filename)             
                if os.path.isfile(self.f):
                    self.lst_of_paths.append(self.f)
        
        for filename in os.listdir(path_to_home):
            self.f_home = os.path.join(path_to_home, filename)
            if os.path.isfile(self.f_home):
                self.lst_of_paths_home.append(self.f_home)

    def move(self):
        for file_path in self.lst_of_paths:
            if not os.path.exists(file_path):
                continue
            for directories in self.dir_dict.keys():
                for formats in self.dir_dict[directories]:
                    current_file = file_path
                    current_name = os.path.basename(current_file)
                    current_directory = directories
                    if current_file.endswith(formats):
                        destination_path = os.path.join(self.home, current_directory, current_name)
                        if not os.path.exists(destination_path):
                            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                            os.rename(current_file, destination_path)

    def move_files_from_home(self):
        for file_path in self.lst_of_paths_home:
            if not os.path.exists(file_path):
                continue
            for directories in self.dir_dict.keys():
                for formats in self.dir_dict[directories]:
                    current_file = file_path
                    current_name = os.path.basename(current_file)
                    current_directory = directories
                    if current_file.endswith(formats):
                        destination_path = os.path.join(self.home, current_directory, current_name)
                        if not os.path.exists(destination_path):
                            os.rename(current_file, destination_path)
    
    def write_logs_to_file(self):
        log_file_path = os.path.join(self.current_path, 'arranger_logs.txt')
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'Arranger Logs - {datetime.now()}:\n')
            for log in self.logs:
                log_file.write(log + '\n')
