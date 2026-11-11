#1 Factorial
n = int(input("Enter a Number:"))
Fact = 1
for i in range(1, n+1):
  Fact = Fact * i
print("Factorial=", Fact)

#2 fibonacci
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#3 Armstrong
num = int(input("Enter a number: "))
original = num
digits = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#4 palindrome
n = int(input("Enter a Number:"))
orginal = n
reverse = 0
while n > 0:
  digit = n % 10
  reverse = reverse * 10 + digit
  n = n // 10
if reverse == orginal:
  print("Palindrome")
else:
  print("Not a Palindrome")

#5 n = int(input("Enter a Number:"))
count = 0
for i in range(1, n+1):
  if n % i == 0:
    count = count + 1
if count == 2:
  print("Prime Number")
else:
  print("Not a Prime Number")

#6 second largest
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

#7 second smallest
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

#8 zeros to end
numbers = [0, 1, 0, 3, 12, 0, 5]
result = []
for i in numbers:
    if i != 0:
        result.append(i)
for i in numbers:
    if i == 0:
        result.append(i)
print(result)

#9 right angled triangle
for i in range(1, 6):
    print("* " * i)
print()

#10 inverted RAT
for i in range(5, 0, -1):
    print("* " * i)
print()

#11 square
for i in range(5):
    print("* * * * *")
print()

#12 left side t
for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)
  
#13 inverted left
for i in range(5, 0, -1):
    print("  " * (5 - i) + "* " * i)

#14 pyramid
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
print()

#15 Inverted pyramid pattern
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
print()

#16diamond
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)
print()

#17 for i in range(4):
    for j in range(6):
        if i == 0 or i == 3 or j == 0 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()


