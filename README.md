# backupscript

Python script to take the backup of directories as a tar file and move to remote server.

## Features

* Take the backup of multiple directories as a tar file
* Copy to remote server
* Remove the local copy of backup

### Configure

```
Replace the value of SOURCES with the absolute path of directories which required to add to tar
We can use compression methods like gz,bz2 as per the requirement, 
  >> tarFilename,'w:gz'
  >> tarFilename,'w:bz2'
Replace the values of the following,
HOST = '192.168.1.105'  >> Remote host 
USER = 'sdteam'
PASSWORD = 'wewgewhgh!22121'
PORT = 22
REMOTEDIR = '/home/server/testsftp'

```
