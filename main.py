import sys
import os
import json
import shutil
from pathlib import Path
from arranger import Arranger

def get_home_directory():
    if len(sys.argv) > 1 and sys.argv[1] == '-i':
        return input('Enter your home directory: ')
    return sys.argv[1] if len(sys.argv) > 1 else ''

def main(home_directory=None):
    home = get_home_directory()
    config_path = str(Path.home()) + '/.config/arranger'
    Path(config_path).mkdir(exist_ok=True, parents=True)

    if home:
        if os.path.exists(home):
            if not os.path.isfile(config_path + '/config.json'):
                shutil.copy(os.path.dirname(__file__) + '/config.json', config_path + '/config.json')
            with open(config_path + '/config.json', 'w') as outfile:
                json.dump({"path": str(home)}, outfile)
        else:
            print(f'"{home}" directory does not exist.')
            return

    arranger = Arranger(home)
    arranger.verify()
    arranger.get_files()
    arranger.move()
    arranger.move_files_from_home()
    arranger.write_logs_to_file()
    print('Your files are now organized!')

if __name__ == '__main__':
    main()
