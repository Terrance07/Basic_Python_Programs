start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
def count_odd(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            count = count + 1
    return count
print("Odd numbers count =", count_odd(start, end))
