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



