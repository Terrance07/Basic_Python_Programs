start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total = total + i
    return total
print("Sum =", sum_range(start, end))
