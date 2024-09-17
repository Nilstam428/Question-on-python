# write mode

# concept 1
# if file open with write mode
# 1. file alrady exist = data will be override


# with open("jp.txt", "w") as file:
#     pass

# concept 2

# if file open with write mode then file will be created

# with open("niles.css", "w") as file:
#     pass


# concept 3
# data will be written from starting

# with open("jp.py", "w") as f:
#     f.write("this is some random data")


# 1. write()
# 2. writelines()

# with open("jp.py", "w") as f:
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")
#     f.write("this is some random data \n")


# l1 = [
#     "this is first line \n",
#     "this is first line \n",
#     "this is first line \n",
#     "this is first line \n",
# ]

# with open("jp.py", "w") as file:
#     file.writelines(l1)
