student={
    "name":"Rahul",
    "age":22
}

print(student.get("marks"))# it returns none(not an error)
print(student.get("city","Bengaluru"))# it gives the default value Bengaluru

print(student.get("name","not provided"))
print(student.get("email","not provided"))