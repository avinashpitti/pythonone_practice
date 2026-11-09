def greet(name):
    # return "Hello, "+name+"!"
    return f"Hello, {name}!"
print(greet("Asha"))


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))