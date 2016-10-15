import os

from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

def make_directory_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)

file_id = "1VgLPhOuiLwOjMhdb9sXDkumn9AjFae0tX-ABBFOp1iI"

parents = []
isroot = False

while isroot == False:

    file = drive.CreateFile({'id': file_id})
    p1 = file['parents']
    p2 = p1[0]
    p = p2['parentLink']
    parent_id = p[p.rfind('/')+1:]
    file1 = drive.CreateFile({'id': parent_id})
    parent = file1['title']

    print(file['title'].ljust(60), file['mimeType'].ljust(40), parent)
    file_id = parent_id
    parents.append(parent)
    isroot = p2['isRoot']

parents[-1:] = ["Google Drive Download"]

path = "D:\\Google Drive\\"
for s in parents[::-1]:
    path = path + (s + '\\')

#path = '"' + path[:-1] + '"'
path = path[:-1]
print(path)

make_directory_if_not_exists(path)

"""
mkdir = 'mkdir ' + path
print(mkdir)
# print(p[p.rfind('/')+1:])         


# Auto-iterate through all files that match this query
file_list = drive.ListFile({'q': "title = " + file_id}).GetList()
for f in file_list:
  print('title: %s, mimeType: %s, id: %s' % (f['title'], f['mimeType'], f['id']))
  filelist.append({"title":f['title'],"MimeType":f['mimeType'],"id":f['id']})
"""

