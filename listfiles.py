drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'MarcelSchlatterAddressTelephone.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Brunnenwiesenstrasse 25, 8212 Neuhausen am Rheinfall') # Set content of the file from given string.
file1.Upload()

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))