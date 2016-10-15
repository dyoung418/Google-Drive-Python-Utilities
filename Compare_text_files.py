file1 = "D:/Google Drive/Python/PyDrive/file_id_list_SOURCE.txt"
file2 = "D:/Google Drive/Python/PyDrive/file_id_list_TARGET.txt"

f1 = open(file1, "r")
f2 = open(file2, "r")
f1_lines = [line for line in f1 if line.strip()] # omit empty lines and lines containing only whitespace
f2_lines = [line for line in f2 if line.strip()] # omit empty lines and lines containing only whitespace

j = 0
miss = False

for l1 in f1_lines:
    i = 0
    j = j+1
    found = False
    for l2 in f2_lines:
        i = i+1
        if (l1[:25] == l2[:25]): # compare only first 25 characters on each line
            # print(l1 + "from file1 found in file2 at line " + str(i))
            found = True
    if found == False:
        print("line " + str(j) + " \n" + l1[:25] + " not found in file2")
        miss = True

if miss == False:
    print("all lines from file1 found in file2")
    
f1.close()
f2.close()