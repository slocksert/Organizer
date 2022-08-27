import sys
import arranger as a
import os
import json
from pathlib import Path
import shutil

def main():
    home = ''
    dashs = '-' * 27
    current_path = os.path.dirname(__file__)
    config_path = str(Path.home()) + '/.config/arranger'

    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == '-i':
            home = input(f'{dashs}\nEnter your home directory:\n{dashs}\n->')
            dictionary = {"path":str(home)}
            if os.path.exists(home):
                with open('config.json', 'w') as conf:
                    json.dump(dictionary, conf)
                if not os.path.isfile(config_path + '/config.json'):
                    shutil.copy(current_path + '/config.json', config_path + '/config.json')
                with open(config_path + '/config.json', 'w') as outfile:
                    json.dump(dictionary, outfile)
        else:
            home = parameter

    arranger = a.Arranger(home)
    arranger.verify()
    arranger.get_files()
    arranger.move()
    arranger.move_files_from_home()

if __name__ == '__main__':
    main()