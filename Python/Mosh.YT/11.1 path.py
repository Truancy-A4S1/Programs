from pathlib import Path #Path is an object


#absolute path - start from root (c:/ or d:/)

#relative path - starting from current directory
path = Path("D:\Programs\Python\Mosh.YT\ecommerce")
print(path.exists()) #check if path exists

path1 = Path("test email")
print(path1.mkdir()) #crate a directory

#print(path1.rmdir()) #remove a directory

#check the files from directory
path2 = Path("D:\Programs\Python\Mosh.YT")
print(f'ALL .PY FILES')
for file in path2.glob("*.py"): #all .py files in the directory
    print(file)

print(f'ALL FILES')
for file in path2.glob("*"): #all files in the directory
    print(file)