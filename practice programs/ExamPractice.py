# friends =['Joseph','Glenn','Sally']
# for friend in friends:
#     print("hello :",friend)

# money = 100
# if money :
#     print("maf")
# else:
#     print("abc")


# fruits =["apple","banana","cherry"]
# for x in fruits:
#     print(x)


# for x in "banana":
#     print(x)


# adj =["red","big","tasty"]
# fruits=["apple","banana","cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)


# row = int(input("Enter the number of rows:"))
# for i in range(1,row +1):
#     for j in range(1,i+1):
#         print('*' ,end=' ')


# rows = int(input('Enter the number of rows: '))
# # outer loop
# for i in range(1, rows + 1):
#     # nested loop
#     for j in range(1, i + 1):
#         # display number
#         print('*', end='')
#     # new line after each row
#     print('')


# fruits =["apple","banana","cherry"]      
# #Explanation:

# #The loop iterates through the fruits list.
# #For each item (x), the condition if x == "banana": is checked.
# #If the item is "banana", the break statement is executed, terminating the loop immediately.
# #The print(x) statement is only executed if the loop hasn’t broken yet.
# for x in fruits:
#     if x=="banana":
#         break
#     print(x)


# fruits =["apple","banana","cherry"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break


# for i in range(1,6):
#     print("6 *",i,"=",6*i)
# print("stop")

# i =1
# while i<=5:
#     print("6 *",i,"=",6*i)
#     i+=1



# num = 0
# while num < 10:
#     num += 1
#     if (num % 2) == 0:
#         continue
#     print(num)


# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)



# a ="my name is Karthik"
# print(a[1:len(a)])



# a ="    my name is Karthik"
# print(a.strip())  #removes whitespace from the beginning


# a ="my name is Karthik"
# print(a.split(" ",4))



# tup =("a","b","c")
# print(tup[:2])




# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print (dict[Name])
# print (dict['Age'])


# name = "geeks FOR geeks"
# print(name.capitalize())



# string = "geeks for geeks"
# new_string = string.center(  100, ' ')
# print(new_string)

# f = open("practice", "r")
# print(practice())



# def sum(*args):
#     total =0
#     for arg in args:
#         total += arg
#     return total

# print(sum(1,4,6,7))



# def total_fruits(**kwargs):
#     print(kwargs,type(kwargs))


# print(total_fruits(apple=7,banana=9))
        
# class student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def student_details(self):
#         print(f"student {self.name} grade is {self.grade}")
# student1 =student("karthik",19)
# student2 =student("gagan",18)
# student3= student("lallan",14)
# # print(student1.name,student1.grade)
# student1.student_details()
# student2.student_details()
# student3.student_details()



# numbers=[]
# n=int(input("enter the size of the list : "))
# while True:
#     if n>0:
#         i =int(input("enter the element to insert : "))
#         numbers.append(i)
#         n=n-1
#     else:
#         print("n>0")




# f = open('practice.txt', 'w')
# f.write("python is very intresting")
# f.close()

# f=open('practice.txt','r')
# print(f.read())

# f.close()
        


with open("practice.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
