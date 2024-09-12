# Q15. explain multiple inheritance ?


# class A:
#     def m1(self):
#         print("method 1")


# class B:
#     def m2(self):
#         print("method 2")


# class C(A, B):
#     def m3(self):
#         print("method 3")


# obj = C()

# obj.m1()
# obj.m2()
# obj.m3()


# class A:
#     def m1(self):
#         print("method 1")


# class B:
#     def m1(self):
#         print("method 2")


# class C(B, A):
#     def m3(self):
#         print("method 3")


# obj = C()

# obj.m1()


class A:
    def m1(self):
        print("method 1")


class B:
    def m1(self):
        print("method 2")
        # super().m1()


class C(B, A):
    def m3(self):
        print("method 3")
        super().m1()
        A().m1()


obj = C()

obj.m3()
