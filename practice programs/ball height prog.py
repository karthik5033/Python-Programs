#declare a value
a = -16
#read velocity from the user
b = int(input("Enter the velocity : ")) 
#Read players height
pHeight=float(input("enter the players height : "))
#to calculate time ,use the formula:
t = float(-b/(2*a))
print("time :",t,"seconds")
#to calculate height use formula
h=(a*(t**2))+(b*t)
print("height is:",h,"feet")
#add players height with ball height
h = h+pHeight
print("total height is : ",h,"feet")