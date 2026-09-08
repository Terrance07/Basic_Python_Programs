num = int(input("Enter a Number:"))
def Mul_of_Digits(num):
  total = 1
  while num > 0:
    total = total * num %10
    num = num // 10
  return total
print( Mul_of_Dogits(num))
