num = int(input("Enter number of terms: "))
def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        c = a + b
        a = b
        b = c
fibonacci(num)
