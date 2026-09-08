num = int(input("Enter a Number:"))
def sum_of_digits(num):
  total = 0
  while num > 0:
    total += num%10
    num = num//10
  return total
print(sum_of_digits(num))
  
