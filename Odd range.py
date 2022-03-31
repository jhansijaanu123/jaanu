# to print all odd numbers in a range


lower_limit=int(input("enter the lower limit:"))
upper_limit=int(input("enter the upper limt:" ))
for i in range(lower_limit,upper_limit+1):
    if(i%2 !=0):
        print(i)
        