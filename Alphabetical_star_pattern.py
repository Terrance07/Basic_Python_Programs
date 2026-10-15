#A
for i in range(5):
    for j in range(5):
        if ((j == 0 or j == 4) and i != 0) or (i == 0 and 0 < j < 4) or i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#B
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 or i == 2 or i == 4) and j < 4 or (j == 4 and i in [1, 3]):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#C
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#D
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 or i == 4) and j < 4 or (j == 4 and i in [1, 2, 3]):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#E
for i in range(5):
    for j in range(5):
        if i == 0 or i == 2 or i == 4 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#F
for i in range(5):
    for j in range(5):
        if i == 0 or i == 2 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#G
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or (i == 2 and j >= 2) or (j == 4 and i >= 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#H
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#I
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#J
for i in range(5):
    for j in range(5):
        if i == 0 or j == 4 or (i == 4 and j < 4) or (j == 0 and i == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#L
for i in range(5):
    for j in range(5):
        if j == 0 or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#O
for i in range(5):
    for j in range(5):
        if (i == 0 or i == 4) and j in [1, 2, 3] or (j == 0 or j == 4) and i in [1, 2, 3]:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#P
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 or i == 2) and j < 4 or (j == 4 and i == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#S
 for i in range(5):
    for j in range(5):
        if i == 0 or i == 2 or i == 4 or (j == 0 and i == 1) or (j == 4 and i == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#T
for i in range(5):
    for j in range(5):
        if i == 0 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#U
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#X
for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Y
for i in range(5):
    for j in range(5):
        if (i < 3 and (j == i or j == 4 - i)) or (i >= 2 and j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Z
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or i + j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
