#ex 1
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
num = 8
factorial = calculate_factorial(num)
print(f"The factorial of {num} is {factorial}") 
#принимает положительное и целое число и возвращает его факториал

#ex 2
def reverse_string(s):
    reversed_str = ""
    
    for char in s[::-1]:
        reversed_str += char

    return reversed_str
# Example
original_string = "hello"
reversed_string = reverse_string(original_string)
print(f"The original string: {original_string}")
print(f"The reversed string: {reversed_string}")

#ex 3
def get_max(a, b, c):
    return max(a, max(b, c))
# Example
num1 = 10
num2 = 5
num3 = 8
maximum = get_max(num1, num2, num3)
print(f"The maximum among {num1}, {num2}, and {num3} is {maximum}")

#ex 4
def is_even(n):
    return n % 2 == 0
# Example 
num = 10
result = is_even(num)
print(f"The number {num} is even: {result}")

#ex 5
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
# Example 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#ex 6
def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]
# Example 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)

#ex 7
from collections import Counter

def word_frequency(input_string):
    words = input_string.split()
    word_count = Counter(words)
    return word_count
# Example
input_string = "hello world hello python world"
frequency_dict = word_frequency(input_string)
print("Word frequency dictionary:", frequency_dict)

#ex 8
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Example
n = 7
fibonacci_number = fibonacci(n)
print(f"The {n}th Fibonacci number is {fibonacci_number}")

#ex 9
def calculate_running_average(numbers):
    running_sum = 0
    running_average_list = []
    for i, num in enumerate(numbers, start=1):
        running_sum += num
        running_average = running_sum / i
        running_average_list.append(running_average)
    return running_average_list
#Example
numbers = [1, 2, 3, 4, 5]
running_average = calculate_running_average(numbers)
print("Running average:", running_average)