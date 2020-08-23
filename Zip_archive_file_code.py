from shutil import make_archive
from zipfile import ZipFile

with ZipFile('testzip.zip', 'w') as newzip:
    newzip.write('newfile.txt')
    newzip.write('textfile.txt.bak')

