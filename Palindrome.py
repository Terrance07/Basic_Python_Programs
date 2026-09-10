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
