num = int(input("Enter a number: "))
largest = -1
second_largest = -1
while num > 0:
    digit = num % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    num = num // 10
print("Second largest digit:", second_largest)
