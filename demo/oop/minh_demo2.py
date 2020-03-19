class Base:
    def fun(self):
        print("Base.fun()")


class A(Base):
    def fun2(self):
        print("A.fun()")


class B(Base):
    def fun(self):
        print("B.fun()")


class C(A, B):
    def funny(self):
        print("C.fun()")


print(C.mro())
# obj = C()
# obj.fun()

