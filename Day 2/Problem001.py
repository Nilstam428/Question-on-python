# Q create a function to add two numbers and store result in 'result' variable.
# create a another function which double value of 'result'


def add(a, b):
    global result
    result = a + b
    return result


print(add(10, 20))


def double(value):
    return value * 2


print(double(result))


# concept 1

# scope of variable
# 1. global variable = it declare outside of a function
# 2. local variable = it declare inside a function

# name = "ram"


# def funt():
#     value = "100"


# print(name)  # ram
# print(value)  # error throw

# concept 2
# global = convert local variable to global
