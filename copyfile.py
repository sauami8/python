# source: /Users/sauami/Documents/Python
# tareget: /Users/sauami/Documents/Python

import shutil
# shutil.submodule_name(arguments passed)
import os


source =  '/Users/sauami/Documents/Amita/'
target = '/Users/sauami/Documents/Notes/'
# shutil.copy(source, target)

# Fetch the all files from source directory

files = os.listdir(source)

for file_name in files:
    shutil.copy(source+file_name, target+file_name)
    print('Files name in source directories are >', source+'/'+file_name)
print('Files are copied')