a=[1,2,3]
b=a
b.append(4)
print(a)

x=10
def f():
    x=20
    print(x)
f()
# print(x)

print(list("abc"))

print(bool([]))
print(bool((0)))
print(bool([0]))
print(bool({0}))


class Dog():
    def __init__(self,name):
        self.name=name
d=Dog("Rex")
print(d.name)