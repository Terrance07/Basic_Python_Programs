positive = 0
negative = 0
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input("Enter a number: "))
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1
print("Positive numbers =", positive)
print("Negative numbers =", negative)
