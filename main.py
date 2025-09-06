from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
    readFileAndFolder()
    try:
        name = input("Enter the name of your file: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Enter the text you want to enter in file: ")
                fs.write(data)
                print("FILE CREATED SUCCESSFULLY")
        else:
            print("The file already exists")
    except Exception as err:
        print(f"{err} has occurred")

def readFile():
    try:
        readFileAndFolder()
        name = input('Enter the name of file you want to read: ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY")
        else:
            print("The file does not exist")   
    except Exception as err:
        print(f"{err} has occurred")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("For renaming, press 1")
            print("For overwriting, press 2")
            print("For appending, press 3")

            res = int(input("Enter a response: "))
            if res == 1:
                name2 = input("Enter new name: ")
                p2 = Path(name2)
                p.rename(p2)
                print("NAME CHANGED SUCCESSFULLY")
            
            if res==2:
                with open(p,"w") as fs:
                    data = input("Enter the text: ")
                    fs.write(data)
                print("OVERWRITTEN SUCCESSFULLY")

            if res==3:
                with open(p,"a") as fs:
                    data = input("Enter the text: ")
                    fs.write(data)
                print("APPENDED SUCCESSFULLY")

    except Exception as err:
        print(f"{err} has occurred")

def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
        print("FILE REMOVED SUCCESSFULLY")
    except Exception as err:
        print(f"{err} has occurred")
                
print("Type 1 for creating a file")
print("Type 2 for reading a file")
print("Type 3 for updating a file")
print("Type 4 for deleting a file")

check = int(input("Enter your response: "))

if check == 1:
    createFile()

if check==2:
    readFile()

if check==3:
    updateFile()

if check==4:
    deleteFile()