import arranger as a

def main():
    home = input(f'{a.dashs}Enter your home directory:\n')
    arranger = a.Arranger(home)
    arranger.verify()
    arranger.move_files_documents()
    arranger.move_files_music()
    arranger.move_files_pictures()
    arranger.move_files_videos()
    print('Your files are organized now!') 

if __name__ == '__main__':
    main()