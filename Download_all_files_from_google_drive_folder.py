"""
Download all files from a specified Google Drive (identified by its "folder" id)
on my Google Account "marcelschlatter@gmail.com" to D:/Google Drive/Google Drive Download. 

From D:/Google Drive/Google Drive Download the folder is then synced (using Google Drive functionality)
with my Google Drive on marcel@aurum-service.ch

This program should be run in a directory where the file client_secrets.json contains the credential for
my Google Drive on marcelschlatter@gmail.com

In order for the program to run, it may be required to first install pydrive, using the command "pip install PyDrive"
in the Windows Terminal windows (i.e., from where this program is started).

"""

from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

import shutil, os

def Start_download(folder_id):
    List_folder(folder_id)
    # print(filelist)
    for l in reversed(filelist):
        # print(l['title'].ljust(60), l['MimeType'].ljust(35), l['id'].ljust(20))
        if not l['MimeType'][:15]=='application/vnd':
            download = drive.CreateFile({'id': l['id']})
            download.GetContentFile(l['title'], l['MimeType']) # Download file
            print(l['title'] + " downloaded. Mime Type = ", l['MimeType'])
            Move_file(l['id'], l['title'])
    pass

def List_folder(parent):
    # print({'q': "'%s' in parents and trashed=false" % parent})
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
    for f in file_list:
        if f['mimeType']=='application/vnd.google-apps.folder': # if folder
            filelist.append({"id":f['id'],"title":f['title'],"MimeType":f['mimeType'],"list":List_folder(f['id'])})
        else:
            filelist.append({"id":f['id'],"title":f['title'],"MimeType":f['mimeType']})
    return filelist

def Make_directory_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def Move_file(file_id, file_name):
    parents = []
    isroot = False
    file_ID = file_id

    while isroot == False:

        file = drive.CreateFile({'id': file_id})
        p1 = file['parents']
        p2 = p1[0]
        p = p2['parentLink']
        parent_id = p[p.rfind('/')+1:]
        file1 = drive.CreateFile({'id': parent_id})
        parent = file1['title']

        # print(file['title'].ljust(60), file['mimeType'].ljust(40), parent)
        file_id = parent_id
        parents.append(parent)
        isroot = p2['isRoot']

    parents[-1:] = ["Google Drive Download"]

    path = "D:\\Google Drive\\"
    for s in parents[::-1]:
        path = path + (s + '\\')

    #path = '"' + path[:-1] + '"'
    path = path[:-1]
    # print(path)

    Make_directory_if_not_exists(path)

    try:
        shutil.copy(file_name, path)
    except IOError:
        print("Unable to copy file")

    print(file_name.ljust(40) + " " + path.ljust(80) + " " + file_ID)
    os.remove(file_name)
    pass

# folder = "root"
# folder = "0BxhD2G0gO43yVktTZVdvZHFMOUU"
# folder = "0BxhD2G0gO43yT1c2Uk1XcHBhTGc" 	# Foto
# folder = "0BxhD2G0gO43ybzBiN09GVTc0UXc" 		# Folder Fotos 2
folder = "0BxhD2G0gO43yVEwwN2pFU0tqNHM" 		# Fotos aus der Vergangenheit
# folder = "0BxhD2G0gO43yaEV2a0dPalZSS00"   	# Download
# folder = "0BxhD2G0gO43yQmtBRkE4clZkb0U"   	# Test Folder
# folder = "0BxhD2G0gO43yQXpqemhDV1ZpeEk"   	# Versicherungen

filelist=[]

Start_download(folder)





