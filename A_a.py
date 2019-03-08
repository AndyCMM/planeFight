# coding=utf-8
# @Time  :2019-03-05 23:48
# @Author:AndyMing
# @File  :A_a.py


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        A.add(self, m)
        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self), id(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __new__(cls, *args, **kwargs):
        print('I am new')
        return B.__new__(cls)

    def __init__(self):
        super().__init__()
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self), id(self))
        B.add(self, m)
        self.n += 5


# D().add(3)
# print(D)
# print(D().__dict__)

class C:
    pass


def singlepe():
    s = []

    def single():
        if len(s) == 0:
            s.append(C())
            return s[0]
        else:
            return s[0]
    return single


a = singlepe()
b = a()
print(id(b))
c = a()
print(id(c))

