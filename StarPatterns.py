# Square pattern
for i in range(5):
    print("* * * * *")
print()

# Right triangle pattern
for i in range(1, 6):
    print("* " * i)
print()

# Inverted right triangle pattern
for i in range(5, 0, -1):
    print("* " * i)
print()

#pyramid pattern
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
print()

#Inverted pyramid pattern
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
print()

#Diamond pattern
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)
print()

#Right-Aligned Right Triangle Pattern
for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)
print()

#left triangle pattern
for i in range(1, 6):
    print("* " * (6 - i))
print()

#hollow square pattern
for i in range(4):
    for j in range(6):
        if i == 0 or i == 3 or j == 0 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()


#plus pattern
for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



