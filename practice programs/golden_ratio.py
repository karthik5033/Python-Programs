#Read number of series you need 
n =int(input("enter number of series : "))
#golden series
#Iterative method with values saved in list
fiblist=[0,1]
for i in range(0,n):
    fiblist.append(fiblist[i]+fiblist[i+1])
print("series are",fiblist)
#computing the ratio of successive terms in the list of fibonacci numbers
gratio=[fiblist[i]/float(fiblist[i-1]) for i in range(2,len(fiblist))]
print("golden ratio :",gratio)
