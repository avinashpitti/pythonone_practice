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