import json
import os
import shutil
from pathlib import Path

class Arranger:
    
    def __init__(self, home):
        self.lst_of_dir = ['Downloads', 'Pictures', 'Videos', 'Documents', 'Music', 'Desktop']
        self.home = home
        self.documents = ['*.txt', '*.doc', '*.cnf', '*.conf', '*.cfg', '*.log', '*.asc', '*.csv', '*.json', '*.html', '*.epub', '*.ppt', '*.pptx', '*.pdf']
        self.pictures = ['*.jpg','*.jpeg', '*.gif', '*.png', '*.tiff', '*.psd', '*.eps', '*.ai', '*.indd', '*.raw']
        self.videos = ['*.ts', '*.mp4','*.mov', '*.wmv', '*.avi', '*.avchd', '*.flv', '*.f4v', '*.swf', '*.mkv', '*.webm', '*.mpeg-2']
        self.music = ['*.mp3', '*.aac', '*.flac', '*.alac', '*.wav', '*.aiff', '*.dsd', '*.pcm']
        self.downloads = ['*.7z', '*.xz', '*.zip']    
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
            for directories in self.lst_of_dir:
                if os.path.exists(f'{self.home}/{directories}'):
                    continue
                else:
                    os.mkdir(f'{self.home}/{directories}')
        else:
            quit(f'"{self.home}" directory does not exist.')

    def move_files_downloads(self):
        for directories in self.lst_of_dir:
            for formats in self.downloads:
                for p in Path(f'{self.home}/{directories}').glob(formats):
                    file_path = str(p)
                    pos_bar = file_path.split('/')
                    new_file = pos_bar[4]
                    if file_path:
                        shutil.move(file_path, f'{self.home}/Downloads/{new_file}')

        for formats in self.downloads:
            for p in Path(f'{self.home}').glob(formats):
                file_path = str(p)
                pos_bar = file_path.split('/')
                new_file = pos_bar[3]
                if file_path:
                    shutil.move(file_path, f'{self.home}/Downloads/{new_file}')

    def move_files_documents(self):
        for directories in self.lst_of_dir:
            for formats in self.documents:
                for p in Path(f'{self.home}/{directories}').glob(formats):
                    file_path = str(p)
                    pos_bar = file_path.split('/')
                    new_file = pos_bar[4]
                    if file_path:
                        shutil.move(file_path, f'{self.home}/Documents/{new_file}')

        for formats in self.documents:
            for p in Path(f'{self.home}').glob(formats):
                file_path = str(p)
                pos_bar = file_path.split('/')
                new_file = pos_bar[3]
                if file_path:
                    shutil.move(file_path, f'{self.home}/Documents/{new_file}')

    def move_files_pictures(self):
        for directories in self.lst_of_dir:
            for formats in self.pictures:
                for p in Path(f'{self.home}/{directories}').glob(formats):
                    file_path = str(p)
                    pos_bar = file_path.split('/')
                    new_file = pos_bar[4]
                    if file_path:
                        shutil.move(file_path, f'{self.home}/Pictures/{new_file}')
        
        for formats in self.pictures:
            for p in Path(f'{self.home}').glob(formats):
                file_path = str(p)
                pos_bar = file_path.split('/')
                new_file = pos_bar[3]
                if file_path:
                    shutil.move(file_path, f'{self.home}/Pictures/{new_file}')
                    
    def move_files_videos(self):
        for directories in self.lst_of_dir:
            for formats in self.videos:
                for p in Path(f'{self.home}/{directories}').glob(formats):
                    file_path = str(p)
                    pos_bar = file_path.split('/')
                    new_file = pos_bar[4]
                    if file_path:
                        shutil.move(file_path, f'{self.home}/Videos/{new_file}')
        
        for formats in self.videos:
            for p in Path(f'{self.home}').glob(formats):
                file_path = str(p)
                pos_bar = file_path.split('/')
                new_file = pos_bar[3]
                if file_path:
                    shutil.move(file_path, f'{self.home}/Videos/{new_file}')

    def move_files_music(self):
        for directories in self.lst_of_dir:
            for formats in self.music:
                for p in Path(f'{self.home}/{directories}').glob(formats):
                    file_path = str(p)
                    pos_bar = file_path.split('/')
                    new_file = pos_bar[4]
                    if file_path:
                        shutil.move(file_path, f'{self.home}/Music/{new_file}')
        
        for formats in self.music:
            for p in Path(f'{self.home}').glob(formats):
                file_path = str(p)
                pos_bar = file_path.split('/')
                new_file = pos_bar[3]
                if file_path:
                    shutil.move(file_path, f'{self.home}/Music/{new_file}')
        
        print('Your files are organized now!')

dashs = '-' * 27