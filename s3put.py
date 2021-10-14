# s3put.py - Transfers files to Amazon S3

import os.path

import utils.log
import config
from utils.encrypt import getFileHash


log = utils.log.get_logger('s3put')

version = '0.7'

def main():
    import argparse
    import utils.aws
    import utils.filesystem 

    parser = argparse.ArgumentParser(description='''Transfers the given
            file to Amazon S3.''')
    parser.add_argument('--list', action='store_true', help='''If the given
            file is a list of files, send each item in the list. The
            directory tree is preserved so that the files can be restored
            to their original locations.''')
    parser.add_argument('file_path')
    args = parser.parse_args()
    
    key = utils.aws.s3connect()
    key.key = utils.aws.create_file_key(os.path.basename(args.file_path))
    if args.list:
        # key.key is now a folder. We'll modify the key with each upload to
        # place the files within it
        base = os.path.dirname(key.key)

        files = utils.filesystem.read_file_list(args.file_path)
        for f in files:
            f = f.strip()
            key.key = '/' + base + f

            if os.path.isdir(f):
                upload_dir_tree(f, key)
            else:
                key.set_metadata('hash', getFileHash(f))
                key.set_contents_from_filename(f)


def upload_dir_tree(dir_tree, key):
    '''Uploads a directory tree rather than a single file.'''

    def visit(_, dir_tree, files):
        log.debug('dirtree\t%s' % dir_tree)
        k = thekey      # Reset key each entry
        for f in files:
            log.debug('f: %s' % f)
            fp = os.path.join(dir_tree, f)
            if os.path.isfile(fp):
                log.debug('reg f:  %s' % fp)
                # For each file, update the key with the path
                key.key = k + os.path.basename(fp)
                key.set_metadata('hash', getFileHash(fp))
                key.set_contents_from_filename(fp)

    # Execute visit in each directory
    thekey = key.key
    log.debug('uploading tree %s', dir_tree)
    os.path.walk(dir_tree, visit, None)


if __name__ == '__main__':
    main()
