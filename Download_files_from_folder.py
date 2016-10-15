from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

folder_id = "'0BxhD2G0gO43yRUV4YXBoOWVZaTg'" # obtain from print-output of running xxxxxxxxxxxx.py

# Auto-iterate through all files in this folder
file_list = drive.ListFile({'q': folder_id + " in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
    file2 = drive.CreateFile({'id': file1['id']})
    print('title: %s, mimeType: %s' % (file2['title'], file2['mimeType']))
    file2.GetContentFile(file2['title'], file2['mimeType']) # Download file
