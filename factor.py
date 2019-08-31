# Given a number, print its factors

number = int(input("Enter a number "))

def print_factors(num):
    print(f"The factors of  {num} are ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

print_factors(number)