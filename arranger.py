import json
import os
import pathlib
import shutil
from pathlib import Path

class Arranger:
    
    def __init__(self, home):
        self.home = home
        self.dir_dict = {'Downloads':['.7z', '.xz', '.zip', '.rar'], 
        'Pictures':['.jpg','.jpeg', '.gif', '.png', '.tiff', '.psd', '.eps', '.ai', '.indd', '.raw'], 
        'Videos':['.ts', '.mp4','.mov', '.wmv', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.mpeg-2'], 
        'Documents':['.txt','.bak','.xls','.xlsx','.md','.py','.txt', '.doc', '.cnf', '.conf', '.cfg', '.log', '.asc', '.csv', '.json', '.html', '.epub', '.ppt', '.pptx', '.pdf'], 
        'Music':['.mp3', '.aac', '.flac', '.alac', '.wav', '.aiff', '.dsd', '.pcm']}   
        self.config()
        
    def config(self):
        if not self.home == '':
            return
        
        current_path = os.path.dirname(__file__)
        config_path = str(Path.home()) + '/.config/arranger'
        Path(config_path).mkdir(exist_ok=True, parents=True)

        if not os.path.isfile(config_path + '/config.json'):
            shutil.copy(current_path + '/config.json', config_path + '/config.json')
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
                
                if os.path.exists(f'{self.home}/Etc'):
                    continue
                else:
                    os.mkdir(f'{self.home}/Etc')
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
            for directories in self.dir_dict.keys():
                for formats in self.dir_dict[f'{directories}']:
                    current_file = file_path
                    current_name = pathlib.Path(current_file).name
                    current_directory = directories
                    if file_path.endswith(formats):
                        shutil.move(current_file, f'{self.home}/{current_directory}/{current_name}')
                    else:
                        shutil.move(current_file, f'{self.home}/{current_directory}/etc')

    def move_files_from_home(self):
        for file_path in self.lst_of_paths_home:
            for directories in self.dir_dict.keys():
                for formats in self.dir_dict[f'{directories}']:
                    current_file = file_path
                    current_name = pathlib.Path(current_file).name
                    current_directory = directories
                    if file_path.endswith(formats):
                        shutil.move(current_file, f'{self.home}/{current_directory}/{current_name}')
                    else:
                        shutil.move(current_file, f'{self.home}/{current_directory}/etc')