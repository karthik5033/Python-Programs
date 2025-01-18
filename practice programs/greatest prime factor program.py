n =int(input("enter the number :"))
n=int(n)
maxPrime =-1
while n%2==0:
    maxPrime=n
    n=n/2
    print("N:",n)
    print("N1:",n)
for i in range(3,int(n**0.5)+1,2):
    while n%i==0:
        maxPrime=i
        n=n/i
if n>2:
    maxPrime=n
    print("max prime factor : ",int(maxPrime))
    

        
