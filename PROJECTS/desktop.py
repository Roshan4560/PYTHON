from pathlib import Path

def readfileandfolder():
    path = path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    readfileandfolder()

print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deleting a file ")

check = int(input("Please enter your response : "))

if check == 1:
    createfile()