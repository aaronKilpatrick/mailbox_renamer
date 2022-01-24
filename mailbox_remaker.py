import shutil
import os

filepath = '/home/aaronk/Documents/test/'
newfolder = '/home/aaronk/Documents/newfiles/'

for root, dirs, files in os.walk(filepath, topdown=True):
    for dir in dirs:
        folder_name = dir.split('.', 1)[0]
        original_path = os.path.join(f"{root}{dir}", 'mbox')

        # Copy and rename file into given directory
        try:
            shutil.copyfile(original_path, f'{newfolder}{folder_name}')
        except shutil.Error:
            raise Error(f'Unable to copy file from directory: {foldername}')
        except FileNotFoundError:
            print(f"Could not find directory: \n{newfolder}")
            break