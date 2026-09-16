num = int(input("Enter a number: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
