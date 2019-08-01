#program to print pattern
n = int(input("Enter the number of rows"))
i = 0

while i<n:
    j = 0
    while j<i:
        print("*",end="")
        j+=1
    print()
    i+=1
