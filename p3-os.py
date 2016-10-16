#in p3 and p2

import os

print(dir(os))
print('Curent working directory: ' + os.getcwd())
help(os)

import shutil

print('-'*20)
print(dir(shutil))

print('\nWe use shutil.copyfile and shutil.move to do file copy and file move correspondingly\n')

import glob

print('See the list of python files in this folder: ')
print(  glob.glob('*.py'))


import sys

print('Arguements passed to the pgm : ' + str(sys.argv))
sys.stderr.write('Warning!!! Log file not found... Starting a new one -- Used to print warnings or errors directly on screen even\
if standard output has been redirected\n')
