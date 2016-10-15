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

filelist=[]

# parent_id = "'root'"
# parent_id = "'1WQPZr0Hc_ly2vaCZx0o2cfT7G6yuUg'"   # Google Photos
# parent_id = "'0BxhD2G0gO43ybzBiN09GVTc0UXc'" # Folder Fotos 2
# parent_id = "'0BxhD2G0gO43yaEV2a0dPalZSS00'"   # Download
# parent_id = "'0BxhD2G0gO43yQmtBRkE4clZkb0U'"   # Test Folder
parent_id = "'0BxhD2G0gO43ybkZTd2VVcTVyYVE'"   

# Auto-iterate through all files that match this query
file_list = drive.ListFile({'q': parent_id + " in parents and trashed=false"}).GetList()
for f in file_list:
  # print('title: %s, mimeType: %s, id: %s' % (f['title'], f['mimeType'], f['id']))
  filelist.append({"title":f['title'],"MimeType":f['mimeType'],"id":f['id']})

f = open("file_id_list.txt", "w")

for l in filelist:
   print(l['title'].ljust(60), l['MimeType'].ljust(35), l['id'].ljust(20))
   f.write(l['title'].ljust(60) + l['id'].ljust(20) + "\n")