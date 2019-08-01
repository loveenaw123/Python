#program to print the first number divisible by 5 in python
nums = [12,15,16,25,24,30]
for i in nums:
  if i%5==0:
     print(i)
     break
else:
    print("not found")
