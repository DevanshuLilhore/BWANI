# add two num
def sum(n1,n2):
    if n2==0:
        return n1
    else:
        return sum(n1+1,n2-1)
n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
s=sum(n1,n2)
print("sum of {} and {} is {} ".format(n1,n2,s))

# big number find between two number
n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
s=n1 if n1>n2 else n2
print("Between {} and {} big number : {} ".format(n1,n2,s))

# use of lambda function big number find between two number
n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
s=lambda a,b: n1 if n1>n2 else n2
print("Between {} and {} big number : {} ".format(n1,n2,s(n1,n2)))
