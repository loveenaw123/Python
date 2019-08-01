#program to print perfect squares from 0 to n
n = int(input("Enter any number"))
for i in range(n):
    sq = i*i
    print(sq)
    if sq==n:
        break;
