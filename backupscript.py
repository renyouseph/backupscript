############ This python scrpit is used take the backup of directories as a tar file and move to remote server #######
#
# Created by Reny Ouseph
# Created on 17-07-2018
#
#### Requirements #####################
# apt-get install python3
# apt-get install python3-pip
# pip3 install pysftp
#######################################


import os
import tarfile
import pysftp
import time
import glob

HOST = '192.168.0.105'
USER = 'user'
PASSWORD = 'wrt%2132'
PORT = 22
REMOTEDIR = '/home/user/testsftp'

SOURCES = [ '/root/python/files/' ]

for source in SOURCES:
    if os.path.isdir(source):
        dirName = os.path.basename(source.rstrip('/'))
        timeTag = time.strftime("%Y-%b-%d-%H-%M")
        suffix = 'tar.gz'
        backupName = '{}-{}.{}'.format(dirName,timeTag,suffix)
        tarFilename = '/root/python/tar/{}'.format(backupName)
        print('Creating backupfile : {}'.format(tarFilename))
        with tarfile.open(tarFilename,'w:gz') as tar:
            tar.add(source)
        print('Backup completed')
        sftp = pysftp.Connection(host=HOST,username=USER,password=PASSWORD,port=PORT)
        sftp.cwd(REMOTEDIR)
        sftp.put(tarFilename)
        sftp.close()
        print("Copying backup to Remote server completed")
        os.unlink(tarFilename)
        print("Local backup has been deleted")
