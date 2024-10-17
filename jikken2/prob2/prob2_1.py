# -*- coding: utf-8 -*-
import zipfile

def main():
    zipfilename = 'test1.zip'
    password = "test"
    zip_file = zipfile.ZipFile(zipfilename)
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        print('Password found: %s' % password)
    except:
        print('Wrong password: %s' % password)

if __name__ == '__main__':
    main()