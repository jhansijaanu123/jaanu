# to print all even numbers in a range

lower_limit=int(input("enter the lower limit: "))
upper_limit=int(input("enter the upper limit: "))
for i in range(lower_limit,upper_limit+1):
    if(i%2==0):
        print(i)