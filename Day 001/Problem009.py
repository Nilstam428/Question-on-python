# Q insert element at particuler index (without insert method)


# l1 = [1, 2, 3]
# l1[2] = "jp"
# l1.insert(1, "jd")
# print(l1)

# 1. list = mutable data type (value change )


# Q how to add element in  list at last position.


l1 = [10, 20, 30, 40, 50]
ins = int(input("Enter an index to insert: "))

value = int(input("Enter a value to insert: "))

l1.append(0)
for i in range(len(l1) - 1, ins, -1):
    l1[i] = l1[i - 1]

l1[ins] = value

print("List after insertion:", l1)
