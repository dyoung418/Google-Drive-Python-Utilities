file_name = "D:/Google Drive/Python/PyDrive/file_id_list_WED_TARGET.txt"

file = open(file_name, "r")
file_lines = [line for line in file if line.strip()] # omit empty lines and lines containing only whitespace

j = 0
duplicates = []

for l1 in file_lines:
    i = 0
    j = j+1
    found = False
    for l2 in file_lines:
        i = i+1
        if (l1[:25] == l2[:25]) and ((i == j) == False): # compare only first 25 characters on each line
            duplicates.append(l1[:20] + " duplicate lines " + str(i) + " and " + str(j))

if (len(duplicates)) > 0:
    print('\n'.join(sorted(duplicates)[::2]))
else:
    print("no duplicates found")
    
file.close()