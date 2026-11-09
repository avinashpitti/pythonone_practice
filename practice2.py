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


def largest(numbers):
    largest_num=numbers[0]
    for num in numbers:
        if num>largest_num:
            largest_num=num

    return largest_num
print(largest([23,1,45,33,90,56,13]))
print(largest([4,2,3,5,1]))