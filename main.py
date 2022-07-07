#!/bin/python3
import sys
import arranger as a

def main():
    home = ''
    if len(sys.argv) > 1:
        parameter = sys.argv[1]
        if parameter == '-i':
            home = input(f'{a.dashs}\nEnter your home directory:\n{a.dashs}\n->')
        else:
            home = parameter

    arranger = a.Arranger(home)
    arranger.verify()
    arranger.move_files_documents()
    arranger.move_files_music()
    arranger.move_files_pictures()
    arranger.move_files_videos()

if __name__ == '__main__':
    main()