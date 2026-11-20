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