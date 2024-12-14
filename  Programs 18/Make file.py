import os

def New_file():
    no_file = input("Enter 1 for make any file\n2 for make folder: ")
    if(no_file == "1"):
        no_file = input("Enter how much file you want to made in the form of numbering\nlike: file 1, file 2 etc: ")
        print(" Note: The Default location is 'D' and if you want to further inside the folders you should enter folder name in which you want to make file\n if folder in folder use'/' like, folder_name1/folder_2")
        file_path = input("Enter file path: ")
        file_name = input("Enter file name you want to make: ")
        format= input("Enter format like: .txt, .py, .etc: ")
        complete_path = f'D:/{file_path}'
        try:
            if not os.path.exists(complete_path):
                os.makedirs(complete_path)
                
            for i in range(1, int(no_file) + 1):
                full_file_path = os.path.join(complete_path, f'{file_name} {i}{format}')
                with open(full_file_path, 'w') as file:
                    pass  # Just creating empty files

            print("Files created successfully")

        except OSError as e:
            print(f"Error creating the file: {e}")

    elif(no_file == "2"):

        no_file = input("Enter how much folder you want to made in the form of numbering\nlike: file 1, file 2 etc: ")
        print(" Note: The Default location is 'D' and if you want to further inside the folders you should enter folder name in which you want to make file\n if folder in folder use'/' like, folder_name1/folder_2")
        file_path = input("Enter folder path: ")
        file_name = input("Enter folder name: ")
        complete_path = f'D:/{file_path}'
        try:
            if not os.path.exists(complete_path):
                os.makedirs(complete_path)
            for i in range(1, int(no_file) + 1):
                full_file_path = os.path.join(complete_path, f'{file_name} {i}')
                os.mkdir(full_file_path)

            print("Folders created successfully")

        except OSError as e:
            print(f"Error creating the file: {e}")
    else:
        print("Please only enter 1 or 2..")

def Rename():
    no_file = input("Enter how much folder you want to made in the form of numbering\nlike: file 1, file 2 etc: ")
    print(" Note: The Default location is 'D' and if you want to further inside the folders you should enter folder name in which you want to make file\n if folder in folder use'/' like, folder_name1/folder_2")
    file_path = input("Enter file path: ")
    old_file_name = input("Enter file old name: ")
    format = input("Enter the file format (e.g., .txt, .py, etc.) or leave it blank if deleting folders: ")
    new_file_name = input("Enter file new name: ")
    format_new = input("Enter the file new format (e.g., .txt, .py, etc.) or leave it blank if deleting folders: ")
    complete_path = f'D:/{file_path}'
    try:
        if os.path.exists(complete_path):
            for i in range(1, int(no_file) + 1):
                if format:
                    full_file_path = os.path.join(complete_path, f'{old_file_name} {i}{format}')
                    new_full_path = os.path.join(complete_path, f'{new_file_name} {i}{format_new}')
                    os.rename(full_file_path, new_full_path)
                else:
                    full_file_path = os.path.join(complete_path, f'{old_file_name} {i}')
                    new_full_path = os.path.join(complete_path, f'{new_file_name} {i}')
                    os.rename(full_file_path, new_full_path)
                    
            print("Files/Folders renamed successfully")
        else:
            print("The specified path does not exist.")

    except OSError as e:
        print(f"Error creating the file: {e}")

def Delete():
    no_file = input("Enter how much file you want to delete in the form of numbering\nlike: file 1, file 2 etc: ")
    print(" Note: The Default location is 'D' and if you want to further inside the folders you should enter folder name in which you want to make file\n if folder in folder use'/' like, folder_name1/folder_2")
    file_path = input("Enter file path: ")
    file_name = input("Enter file or folder name which you want to remove: ")
    format = input("Enter the file format (e.g., .txt, .py, etc.) or leave it blank if deleting folders: ")
    complete_path = f'D:/{file_path}'
    try:
        if os.path.exists(complete_path):
            for i in range(1, int(no_file) + 1):
                full_file_path = os.path.join(complete_path, f'{file_name} {i}{format}')
                
                if format:
                    os.remove(full_file_path)  # Deleting file
                else:
                    os.rmdir(full_file_path)  # Deleting folder
            
            print("Files/Folders deleted successfully")
        else:
            print("The specified path does not exist.")
            
    except OSError as e:
        print(f"Error deleting the file: {e}")
while True:

    print("Enter 1 for make any new file or folder")
    print("Enter 2 for rename any new file or folder")
    print("Enter 3 for delete any new file or folder")
    print("Enter 4 for exit")

    choice = input("Enter yuor choice between 1-4: ")

    if (choice == "1"):
        New_file()

    elif (choice == "2"):
        Rename()

    elif (choice == "3"):
        Delete()
    
    elif (choice == "4"):
        break

    else:
        print("Please only enter between 1-3")