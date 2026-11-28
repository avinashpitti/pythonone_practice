student={
    "name":"Rahul",
    "age":22
}

print(student.get("marks"))# it returns none(not an error)
print(student.get("city","Bengaluru"))# it gives the default value Bengaluru

print(student.get("name","not provided"))
print(student.get("email","not provided"))

for index,value in enumerate(['A','B','C'],start=1):
    print(index,value)

x='apple,banana,mango'
print(x.split(','))

y=10
print('Value:{}'.format(y))

z={'a':10,'b':20}
print(list(z.keys()))
print(list(z.values()))
print(list(z.items()))
print(z.keys())
print(z.values())
print(z.items())


for key in z:
    print(key)

for value in z.values():
    print(value)

for item in z.items():
    print(item)

x='banana'
print(x.count('a'))
print(x.count('b'))
print(x.count('n'))


for m in range(10,0,-2):
    print(m)


print('hello'.find('z'))

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


name='Python'
def reversing_string(name):
    result=''
    for char in name:
        result=char+result
    return result
print(reversing_string(name))


funcs=[lambda: i for i in range(3)]
print([f() for f in funcs])

fun=[lambda i=i:i for i in range(3)]
print([f() for f in fun])


from decimal import Decimal
print(Decimal("0.1")+Decimal("0.2"))

import copy
a=[[1,2],[3,4]]
b=a.copy()
b[0][0]=99
print(a) # shallow copy changes


c=copy.deepcopy(a)
c[0][0]=0
print(a) # deep copy doesn't changes

print(7/2)
print(7//2) # floor division
print(7%2)
print(-7//2) # floor division

x=6
print(not 1<x<10)

d={}
print(type(d))

for i in enumerate(['a','b']):
    print(i)


print(2==2.0)
print(bool(""))
print(list(zip([1,2],['a','b'])))

print(any([0,0,1]))
print(all([1,0,1]))

print(int('1000',2))

print(1 if 0 else 2)

print([x for x in range(3)],[x for x in range(3)])
print(type(lambda x:x))
print(list(map(lambda x:x*2,[1,2,3])))
print([1,2,3][-1])
print(True+True)
print("a" in "abc")
print([1,2]+[3,4])
print({1,2}|{2,3})
print({1,2} & {2,3})
print(10//3,10%3)
print(isinstance([],(list,tuple)))
print("abc".find("d"))
print([1,2,3].index(2))
print(0 or "default")
print(sorted("cba"))
print(type(1/2))
print("".join(["a","b","c"]))
print(bool(0))

def gen():
    yield 1
    yield 2
    yield 3
g=gen()
print(next(g))
print(next(g))
print(next(g))

print("-".join(["x","y","z"]))
print(" ".join(["x","y","z"]))
print("".join(["x","y","z"]))

def gen():
    yield 1
    yield 2
g=gen()
print(list(g))

def gen():
    return 1
    yield 2
print(list(gen()))

class C:
    @staticmethod
    def f(x):
        return x * 2

print(C.f(5))