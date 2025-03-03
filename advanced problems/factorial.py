n=int(input("enter the number : "))
fact=n
if (n==0 or n==1):
    fact=1
for i in range(1,n):
    pfact=fact*(n-i)
    fact=pfact
print("factorial is :",fact)



# method 2

n=int(input("enter the number : "))
fact=1
for i in range(n,0,-1):
    fact*=i
print("factorial is :",fact)
