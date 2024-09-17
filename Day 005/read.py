# concept 1
# file handling = file operation(read , write , file name change , file delete , update , etc)


# how to open file

# file = open("jp.txt", mode="r")
# for i in file:  # 3
#     print(i, end="")


# file = open("jp.py", mode="r")
# for i in file:  # 3
#     print(i, end="")


# l1 = [1, 2, 3, 4]
# for i in l1:
#     print(i, end="")


# concept 2
# default mode (read mode)
# jp = open("jp.txt")
# for i in jp:  # 3
#     print(i, end="")

# jp.close()


# concept 3
# file.read()
# jp = open("jp.txt")
# print(jp.read())


# concept 4
# when we open file you must need to close that file

# with open("jp.txt") as file:
#     print(file.read())


# 1. read(indexing) = it will give data
# 2. readline() = it will give only first line
# 3. readlines() = it will also give data and convert into in list


# concept 5

# with open("jp.txt") as file:
#     print(file.read())
# with open("jp.txt") as file:
#     print(file.read(15))
# with open("jp.txt") as file:
#     a = file.readlines()
#     for i in a:
#         print(i, end="")


# concept 6
# if we give indexing in readline it will print line
# with open("jp.txt") as file:
#     print(file.readlines(18))


# with open("jp.txt") as file:
#     print(file.readline(50))


# with open("jd.py") as file:
#     print(file.read())


# concept 7:

# try:
#     with open("jd.py") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file not found")


# try:
#     with open("jd.py") as file:
#         print(file.read())
# except :
#     print("file not found")


# try:
#     with open("jd.py") as file:
#         print(file.read())
# except Exception as e:
#     print(f"error : {e}")
