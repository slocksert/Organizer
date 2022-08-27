import json
import os
import pathlib
import shutil
from pathlib import Path

class Arranger:
    
    def __init__(self, home):
        self.home = home
        self.dir_dict = {'Downloads':['.torrent','.taz','.tar','.lz','.iso','.gz','.7z', '.xz', '.zip', '.rar', '.deb', '.rpm','.exe'], 
        'Pictures':['.jpg','.jpeg', '.gif', '.png', '.tiff', '.psd', '.eps', '.ai', '.indd', '.raw'], 
        'Videos':['.wmv','.ogv','.ts', '.mp4','.mov', '.wmv', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.mpeg-2'], 
        'Documents':['.yml','.yaml','.url','.sh','.rb','.md','.m','.js','.go','.cfg','.email','.css','.crdownload','.bak','.odt','.ods','.txt','.bak','.xls','.xlsx','.md','.py','.txt', '.doc', '.cnf', '.conf', '.cfg', '.log', '.asc', '.csv', '.json', '.html', '.epub', '.ppt', '.pptx', '.pdf','.htm', '.docx'], 
        'Music':['.flp','.flv','.mp3', '.aac', '.flac', '.alac', '.wav', '.aiff', '.dsd', '.pcm'],
        'Etc':['.sql', '.pacman', 'ovpn','.bin','.blend','.bat','.db','.elf','.etl','.godot','.java','.jar','.ldb','.vbox']}   
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
                    if current_file.endswith(formats):
                        shutil.move(current_file, f'{self.home}/{current_directory}/{current_name}')
                    else:
                        continue

    def move_files_from_home(self):
        for file_path in self.lst_of_paths_home:
            for directories in self.dir_dict.keys():
                for formats in self.dir_dict[f'{directories}']:
                    current_file = file_path
                    current_name = pathlib.Path(current_file).name
                    current_directory = directories
                    if current_file.endswith(formats):
                        shutil.move(current_file, f'{self.home}/{current_directory}/{current_name}')
                    else:
                        continue