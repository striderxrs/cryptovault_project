# s3backup.py - Creates archives of files according to a cron-determined
# schedule

import os
import sys

import config
import utils.log
import utils.encrypt

log = utils.log.get_logger('s3backup')

version = '1.1'

def main():
    import argparse

    parser = argparse.ArgumentParser(description='''Creates archives of
            files according to a cron-determined schedule.''')
    parser.add_argument('schedule', choices=['daily', 'weekly', 'monthly'],
            help='Determines which backup file to use.')
    parser.add_argument('--follow-symlinks', action='store_true',
            help='''If given, follows symbolic links. Note that zip
            archives always follow links.''')
    parser.add_argument('--version', action='version', version='s3backup '
            '%s; Suite version %s' % (version, config.version))
    args = parser.parse_args()

    do_backup(args.schedule, args.follow_symlinks)


def do_backup(schedule, follow_links):
    '''Handles the backup.'''
    
    from shutil import rmtree
    import utils.filesystem

    if schedule == 'daily':
        backup_list = config.daily_backup_list
    elif schedule == 'weekly':
        backup_list = config.weekly_backup_list
    else:
        backup_list = config.monthly_backup_list

    try:
        files = utils.filesystem.read_file_list(backup_list)
        archive_path, tar_type = create_archive(files, follow_links)
        if config.enc_backup == True:
            # We don't add the enc extension to the key - the metadata
            # will tell us whether the archive is encrypted.
            enc_file = utils.encrypt.encrypt_file(config.enc_key,
                    archive_path, config.enc_piece_size)
            send_backup(enc_file, tar_type, schedule)
            # Delete the plaintext local version
            os.remove(archive_path)
        else: # Not encrypting
            send_backup(archive_path, tar_type, schedule)

        if config.delete_archive_when_finished == True:
            log.debug('Deleting archive.')
            rmtree(config.dest_location)
    except IOError:
        raise
        log.critical('Cannot open file: %s' % backup_list)
        sys.exit(1) 


def create_archive(files, follow_links):
    """Creates an archive of the given files and stores them in
    the location specified by config.destination. Returns the full path of
    the archive."""

    from time import strftime

    try:
        if not os.path.exists(config.dest_location):
            os.makedirs(config.dest_location)
    except OSError:
        # TODO: Fallback to a tmp directory before failing
        log.critical('Cannot create directory %s' % config.dest_location)
        sys.exit(1)

    if config.compression_method == 'zip':
        archive_type = '.zip'
    else:
        archive_type = '.tar'
        mode = 'w:'
        if config.compression_method != 'none':
            archive_type = archive_type + '.' + config.compression_method
            mode += config.compression_method

    archive_name = ('bak' + strftime('%Y%m%d') + archive_type)
    archive_name = os.path.join(config.dest_location, archive_name)
   
    if config.compression_method == 'zip':
        # zipfile always follows links
        create_zip(archive_name, files)
    else:
        create_tar(archive_name, files, mode, follow_links)

    return archive_name, archive_type


def create_zip(archive, files):
    '''Creates a zip file containing the files being backed up.'''
    import zipfile
    from utils.misc import add_file_hash

    try:
        # zipfile always follows links
        with zipfile.ZipFile(archive, 'w') as zipf:
            zipf.comment = 'Created by CryptoVault'
            for f in files:
                f = f.strip()
                if os.path.exists(f):
                    zipf.write(f)
                    add_file_hash(archive, f)
                    log.debug('Added %s.' % f)
                else:
                    log.error('%s does not exist.' % f)
                
                if zipf.testzip() != None:
                    log.error('An error occured creating the zip archive.')
    except zipfile.BadZipfile:
        # I assume this only happens on reads? Just in case...
        log.critical('The zip file is corrupt.')
    except zipfile.LargeZipFile:
        log.critical('The zip file is greater than 2 GB.'
                ' Enable zip64 functionality.')


def create_tar(archive, files, mode, follow_links):
    '''Creates a tar archive of the files being backed up.'''
    import tarfile
    from utils.misc import add_file_hash

    try:
        with tarfile.open(archive, mode, dereference=follow_links) as tar:
            for f in files:
                f = f.strip()
                if os.path.exists(f):
                    tar.add(f)
                    add_file_hash(archive, f);
                    log.debug('Added %s.' % f)
                else:
                    log.error('%s does not exist.' % f)
    except tarfile.CompressionError:
        log.critical('There was an error compressing the backup archive. '
                'Please try again.')
        sys.exit(1)
    except tarfile.TarError:
        log.critical('There was an error creating the backup archive. '
                'Please try again.')
        sys.exit(1)


def send_backup(path, tar_type, backup_schedule):
    """Uses s3put.py to send a file to Amazon S3"""
    # First we have to create a connection to S3
    from os.path import basename
    import utils.aws
    from utils.misc import get_hash_file_path

    key = utils.aws.s3connect()
    key.key = utils.aws.create_archive_key(tar_type, backup_schedule)
    key.set_metadata('hash', utils.encrypt.get_file_hash(path))
    key.set_metadata('enc', str(config.enc_backup))
    log.debug('key: %s' % key)
    log.debug('meta:enc: %s' % key.get_metadata('enc'))
    key.set_contents_from_filename(path)
    # Use the same name for the hash file, but a '.hash' extension
    key.key = utils.aws.create_archive_key(".hash", backup_schedule)
    key.set_contents_from_filename(get_hash_file_path(basename(path)))


if __name__ == "__main__":
    main()
