smallest = None
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    if smallest is None or num < smallest:
        smallest = num
print("Smallest number:", smallest)
