import shutil
import os

filepath = '/home/aaronk/Documents/test/'
newfolder = '/home/aaronk/Documents/newfiles/'

for root, dirs, files in os.walk(filepath, topdown=True):
    for dir in dirs:
        folder_name = dir.split('.', 1)[0]
        original_path = os.path.join(f"{root}{dir}", 'mbox')

        print(original_path)
        shutil.copyfile(original_path, f'{newfolder}{folder_name}')
        
