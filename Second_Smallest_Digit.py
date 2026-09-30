num = int(input("Enter a number: "))
smallest = 10
second_smallest = 10
while num > 0:
    digit = num % 10
    if digit < smallest:
        second_smallest = smallest
        smallest = digit
    elif digit < second_smallest and digit != smallest:
        second_smallest = digit
    num = num // 10
print("Second smallest digit:", second_smallest)
