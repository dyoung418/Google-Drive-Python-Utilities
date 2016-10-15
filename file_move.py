import shutil, os

src = 'FileMoveTest2.txt'
dst = 'D:/Google Drive/Google Drive Download/Foto/Google Photos/2011/10'

try:
    shutil.copy(src, dst)
except IOError:
    print("Unable to copy file")

os.remove(src)
