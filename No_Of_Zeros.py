count = 0
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input("Enter a number: "))
    if num == 0:
        count = count + 1
print("Number of zeros =", count)
