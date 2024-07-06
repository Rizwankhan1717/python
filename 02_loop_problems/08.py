# 8. Prime Number Checker
# Problem: Check if a number is prime.

prime_num = int(input("Enter number to check if its prime or not : "))

is_prime = True

if prime_num > 1:
    for i in range(2,prime_num):
        if (prime_num % i ) == 0:
            is_prime = False
            break

print(is_prime) 