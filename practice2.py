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


def total(numbers):
    total_sum=0
    for num in numbers:
        total_sum+=num
    return total_sum
print(total([1,2,3,4,5]))
print(total([]))