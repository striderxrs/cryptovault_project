# encrypt.py - Encryption/decryption and hash functions

version = '0.4'

import struct
import log


log = log.get_logger('encrypt')


def encrypt_file(key, filename, piece_size):
    import os
    from Crypto.Cipher import AES

    encryptor = AES.new(key, AES.MODE_CBC)
    # Store the file size for when we decrypt
    fsize = os.path.getsize(filename)
    enc_file = filename + '.enc'
    
    with open(filename, 'rb') as inf:
        with open(enc_file, 'wb') as outf:
            outf.write(struct.pack('<Q', fsize))
            while True:
                piece = inf.read(piece_size)
                if not piece:
                    break
                # The file size must be a multiple of 16 bytes
                elif len(piece) % 16 != 0:
                    try:
                        piece += ' ' * (16 - len(piece) % 16)
                    except TypeError:
                        # For Python 3 - TODO: Test decryptor
                        piece += bytes(' ',
                                'ascii') * (16 - len(piece) % 16)
                outf.write(encryptor.encrypt(piece))
    return enc_file


def decrypt_file(key, encrypted_file, decrypted_file, piece_size):
    '''Decrypts and writes a file. Returns True on success, False on fail'''

    from Crypto.Cipher import AES

    try:
        with open(encrypted_file, 'rb') as inf:
            size = struct.unpack('<Q', inf.read(struct.calcsize('Q')))[0]
            decryptor = AES.new(key, AES.MODE_CBC)

            with open(decrypted_file, 'wb') as outf:
                while True:
                    piece = inf.read(piece_size)
                    if not piece:
                        break
                    outf.write(decryptor.decrypt(piece))
                outf.truncate(size)
        return True
    except:
        return False


def get_file_hash(file, algorithm='MD5'):
    '''Returns a hexadecimal hash of the given file. Currently supported
    algorithms are "SHA256", "SHA512" and "MD5"'''

    def getSHA256(file):
        '''Returns a hexadecimal-format SHA256 hash.'''
        from Crypto.Hash import SHA256

        hash = SHA256.new()
        block_size = hash.block_size

        with open(file, 'rb') as f:
            for piece in iter(lambda: f.read(128 * block_size), ''):
                hash.update(piece)

        return hash.hexdigest()

    def getSHA512(file):
        '''Returns a hexadecimal-format SHA512 hash.'''
        from Crypto.Hash import SHA512

        hash  = SHA512.new()
        block_size = hash.block_size

        with open(file, 'rb') as f:
            for piece in iter(lambda: f.read(128 * block_size), ''):
                hash.update(piece)
        
        return hash.hexdigest()

    def getMD5(file):
        '''Returns a hexadecimal-format MD5 hash.'''
        from Crypto.Hash import MD5

        hash  = MD5.new()
        block_size = hash.block_size

        with open(file, 'rb') as f:
            for piece in iter(lambda: f.read(128 * block_size), ''):
                hash.update(piece)
        
        return hash.hexdigest()
   
    if algorithm == 'SHA256':
        return getSHA256(file)
    elif algorithm == 'SHA512':
        return getSHA512(file)
    elif algorithm == 'MD5':
        return getMD5(file)
    else:
        log.error('Unsupported hash algorithm given.')
        return None
