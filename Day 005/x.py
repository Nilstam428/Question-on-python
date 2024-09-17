# concept 1

# if file open with x mode
# 1. if file already exit = it will give error
with open("niles.py", "x") as file:
    file.write("this is some data")
    pass
