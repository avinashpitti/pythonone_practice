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


def smallest(numbers):
    smallest_num=numbers[0]
    for num in numbers:
        if num<smallest_num:
            smallest_num=num

    return smallest_num
print(smallest([5,7,3,8]))
print(smallest([89,34,56,12,77,55]))


def count_vowels(text):
    count=0
    vowels="aeiou"
    for char in text:
        if char.lower() in vowels:
            count+=1
    return count
print(count_vowels("HI everyone, How Are you"))

def reverse_text(text):
    reversed_str=""
    for char in text:
        reversed_str=char+reversed_str
    return reversed_str
print(reverse_text("python language"))


def is_palindrome(text):
    clean_text=text.lower()
    reversed_str=""
    for char in clean_text:
        reversed_str=char+reversed_str
    return clean_text==reversed_str
print(is_palindrome("Madam"))
print(is_palindrome("Teacher"))
print(is_palindrome("Pop"))


def get_evens(nums):
    evens=[]
    for num in nums:
        if num%2==0:
            evens.append(num)
    return evens
print(get_evens([1,2,3,4,5,6,7,8]))


odd_nums=[1,2,3,4,5,6,7,8,9]
def get_odds(odd_nums):
    odds=[]
    for odd_num in odd_nums:
        if odd_num%2==1:
            odds.append(odd_num)
    return odds
print(get_odds(odd_nums))


def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))
print(factorial(0))


def words_length(text):
    words=text.split()
    lengths=[]
    for word in words:
        lengths.append(len(word))
    return lengths
print(words_length("This is a python learning project"))
