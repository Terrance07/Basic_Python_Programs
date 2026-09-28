total = 0
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total = total + num
    count = count + 1
if count > 0:
    average = total / count
    print("Average =", average)
else:
    print("No numbers were entered")
