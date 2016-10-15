from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)


def ListFolder(parent):
  filelist=[]
  # print({'q': "'%s' in parents and trashed=false" % parent})
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
  print(file_list)
  for f in file_list:
    if f['mimeType']=='application/vnd.google-apps.folder': # if folder
        filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
    else:
        filelist.append(f['title'])
  return filelist

file_list = ListFolder('0BxhD2G0gO43yaEV2a0dPalZSS00')

print(file_list)
"""


file_list = ListFolder('root')

print(file_list)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

file1 = drive.CreateFile({'title': 'MarcelSchlatterAddressTelephone.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Brunnenwiesenstrasse 25, 8212 Neuhausen am Rheinfall') # Set content of the file from given string.
file1.Upload()


# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'0BxhD2G0gO43yaEV2a0dPalZSS00' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  # Create GoogleDriveFile instance with file id of file1.
  file2 = drive.CreateFile({'id': file1['id']})
  print('title: %s, mimeType: %s' % (file2['title'], file2['mimeType']))
# title: HelloWorld.txt, mimeType: text/plain
  file2.GetContentFile(file2['title'], file2['mimeType']) # Download file
# GetContentFile(filename, mimetype=None)
"""