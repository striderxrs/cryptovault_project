# aws.py - Misc AWS utility functions

import config

version = '0.1'

def s3connect():
    '''Create/open a bucket and return the key'''
    import boto
    import boto.s3.key

    s3 = boto.connect_s3(config.aws_access_key_id,
            config.aws_secret_access_key)
    bucket = s3.create_bucket(config.bucket)
    key = boto.s3.key.Key(bucket)
    
    return key


def create_file_key(filename):
    '''Creates the key to use for S3. Key will be
    [machine_name]/YYYYMMDD/filename'''
    from time import strftime
    return ('%s/%s/%s' % (config.machine_name, strftime('%Y%m%d'), 
        filename))


def create_archive_key(file_extension, backup_type):
    '''Creates and returns the key for S3. Key format is
    machine_name/backup_type/YYYYMMDD.file_extension'''
    from time import strftime
    keyname = ('%s/%s/%s%s' % (config.machine_name, backup_type,
        strftime('%Y%m%d'), file_extension))
    return keyname
