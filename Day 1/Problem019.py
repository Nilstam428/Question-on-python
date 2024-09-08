# Q. when we throw two dice then number of unique combination on two dice are


count = 0
for i in range(1, 7):
    for j in range(i, 7):
        print(i, j)
        count += 1
print("number of unique values on two dice are :", count)
