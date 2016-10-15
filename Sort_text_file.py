input_file  = "D:/Google Drive/Python/PyDrive/file_id_list_SOURCE.txt"
output_file = "D:/Google Drive/Python/PyDrive/file_id_list_SOURCE_SORTED.txt"

input = open(input_file, "r")
lines = [line for line in input if line.strip()] # omit empty lines and lines containing only whitespace
lines.sort()

i = 0
output = open(output_file, "w") 
for l in lines:
    output.write(l)
    i = i+1

print("Number of lines:" + str(i))

input.close()
output.close()