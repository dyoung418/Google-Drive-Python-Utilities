"""
Create and print table with Names (titles), MimeTypes, and IDs of folders and files in the Google Drive Folder with "parent_id"
Starting at the top of a Google Drive account by setting parent_id = "'root'" (see line 17)

The table is stored in filelist, and printed on line 33

Note: this Python program should be put and run in the same folder that contains the file "clients_secret.json" which 
contains the credentials for the Google Drive Account
"""

from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

def ListFolder(parent):
  # print({'q': "'%s' in parents and trashed=false" % parent})
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
  # print(file_list)
  for f in file_list:
    if f['mimeType']=='application/vnd.google-apps.folder': # if folder
        filelist.append({"id":f['id'],"title":f['title'],"MimeType":f['mimeType'],"list":ListFolder(f['id'])})
    else:
        filelist.append({"id":f['id'],"title":f['title'],"MimeType":f['mimeType']})
  return filelist


# parent_id = "root"
# parent_id = "0BxhD2G0gO43ybzBiN09GVTc0UXc" # Folder Fotos 2
parent_id = "0BxhD2G0gO43yaEV2a0dPalZSS00"   # Download
# parent_id = "0BxhD2G0gO43yQmtBRkE4clZkb0U"   # Test Folder
# parent_id = "0BxhD2G0gO43yQXpqemhDV1ZpeEk"   # Versicherungen


filelist=[]

ListFolder(parent_id)
# print(filelist)
for l in reversed(filelist):
    print(l['title'].ljust(60), l['MimeType'].ljust(35), l['id'].ljust(20))
    if l['MimeType']=='application/vnd.google-apps.folder':
        Folder_name = "Folder_"+l['title']+"_File_"
    if not l['MimeType'][:15]=='application/vnd':
        download = drive.CreateFile({'id': l['id']})
        download.GetContentFile(Folder_name + l['title'], l['MimeType']) # Download file
        print(Folder_name + l['title'] + " downloaded. Mime Type = ", l['MimeType'])



"""
for l in filelist:
   print(l['title'].ljust(60), l['mimeType'].ljust(35), l['id'].ljust(20))
   if not l['mimeType'][:15]=='application/vnd':
       download = drive.CreateFile({'id': l['id']})
       download.GetContentFile(l['title'], l['mimeType']) # Download file
       print(l['title'] + " downloaded")


# Auto-iterate through all files that match this query
file_list = drive.ListFile({'q': parent_id + " in parents and trashed=false"}).GetList()
for f in file_list:
  # print('title: %s, mimeType: %s, id: %s' % (f['title'], f['mimeType'], f['id']))
  filelist.append({"title":f['title'],"MimeType":f['mimeType'],"id":f['id']})

for l in filelist:
   print(l['title'].ljust(60), l['MimeType'].ljust(35), l['id'].ljust(20))


s"""