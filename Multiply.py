#to find multiply all numbers in the list

def multiplylist(mylist):
    result=1
    for x in mylist:
        result=result*x
    return result
list=[1,2,3,4]
print(multiplylist(list))        