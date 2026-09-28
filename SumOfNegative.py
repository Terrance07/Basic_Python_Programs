total = 0
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input("Enter a number: "))
    if num < 0:
        total = total + num
print("Sum of negative numbers =", total)
