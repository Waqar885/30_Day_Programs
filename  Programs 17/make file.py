import os
# address = '30_Programs/ Programs 18/Name.txt'
print("Enter address in this form: D:/Folder_1/Folder_2/file.txt")
address = input("Enter address of txt file: ")

with open(address, 'r') as file:
    lines = file.readlines()
try:
    if not os.path.exists("D:/All Folders"):
        os.makedirs("D:/All Folders")
    for line in lines:
        file_name = line[:-1]
        path = f"D:/All Folders/{file_name}"
        os.mkdir(path)


except OSError as e:
        print(f"Error: {e}")