# filesystem.py - Filesystem utility functions

version = '0.1'

def read_file_list(file_list):
    '''Reads and returns the list of files.'''
    with open(file_list, 'r') as flist:
        return flist.readlines()
    
