#This is a script to delete file from a directory

import os
if os.path.exists('iPas2.txt'):
    os.remove('iPas2.txt')
elif os.path.exists('iPass.txt'):
    os.remove('iPass.txt')
else:
    print('Oga, I no see this file o')