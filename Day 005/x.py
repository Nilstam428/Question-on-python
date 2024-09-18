# concept 1

# if file open with x mode
# 1. if file already exit = it will give error
# 2. if file not exit then it create a file
# with open("niles.py", "x") as file:
#     file.write("this is some data")
#     pass


# with open("Day 005/Problem001.py") as file:
#     print(file.read())


# with open("D:\python\jp.py", "w") as file:
#     file.write("this is some text ")


# import os

# b = os.getcwd()
# print("Current Working Directory:", b)


import os

os.chdir("c:/Users/dellj/Desktop/python 2.0/Day 001")
print("Changed Directory:", os.getcwd())


# import os

# files = os.listdir(".")
# print("Files and Directories in Current Directory:", files)


# import os

# os.mkdir("Day 006")
# print("Directory Created:", os.listdir("."))


# import os

# os.makedirs("folder1/folder2/folder3")
# print("Nested Directories Created")


# import os

# os.rmdir("Day 006")
# print("Directory Removed:", os.listdir("."))


# import os

# os.removedirs("folder1/folder2/folder3")
# print("Nested Directories Removed")


# import os

# os.rename("Day 006", "jd")
# print("File Renamed:", os.listdir("."))


# import os

# os.remove("jd")
# print("File Removed:", os.listdir("."))


import os

exists = os.path.exists("Problem030.py")
print("Does folder1 exist?", exists)
