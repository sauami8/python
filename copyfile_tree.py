import os
import shutil
# Note copytree works only when destination don't have directory structure exists otherwise it will errorout

source =  '/Users/sauami/Documents/Amita/'
target = '/Users/sauami/Documents/Notes/Tree'

def copy_and_overwrite(source, target):
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)
# shutil.copytree(source, target)
    print('Copy Tree completed successfully')


if __name__ == '__main__':
    copy_and_overwrite(source, target)
