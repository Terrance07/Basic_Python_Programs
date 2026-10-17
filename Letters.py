name = "TERRANCE"

for i in range(5):                    
    for letter in name:              
        for j in range(5):              
            if letter == "T":
                if i == 0 or j == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif letter == "E":
                if i == 0 or i == 2 or i == 4 or j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif letter == "R":
                if j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or (i == 1 and j == 4) or (i == 3 and j == 3) or (i == 4 and j == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif letter == "A": 
                if ((j == 0 or j ==4) and i !=0) or (i == 0 and 0 < j < 4) or i == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif letter == "N":
                if j == 0 or j == 4 or i == j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif letter == "C":   
                if i == 0 or i == 4 or j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ") 
            elif letter == "E":
                if i == 0 or i == 2 or i == 4 or j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

        print(" ", end=" ")
    print()                      
