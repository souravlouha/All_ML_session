#LIST

friends = ["apple","orange",5,34.20,True,False, "sourav"]
print(friends)

friends.append("soumita")#basically .append ; list ar end a kichu add kore dey , 
print(friends)

friends.insert(2,"banana") #basically.insert(index, element) ; list ar index a kichu add kore dey specific index ar pore  ,
print(friends)

l1 = [1,8,25,64,21,32,14]
l1.sort() #sort
print(l1)



#TUPLE


# In Python, mutable objects can be changed after they are created, while immutable objects cannot.
#Mutable:
#Examples: Lists, dictionaries, sets
#You can modify their contents directly, such as adding, removing, or updating elements.
#Immutable:
#Examples: Strings, tuples, numbers
#Once created, their values cannot be changed. Any operation that appears to modify them actually creates a new object.  

a1 = (1) #int
a2 =(1,)#tuple

print(type(a1))
print(type(a2))

a = (1,45,True,"sourav")
print(type(a))




#PRACTICE

#Write a program to store three fruits in a list entered by the user.
fruits=[]
f1 = input("enter fruit name: ")
fruits.append(f1)
f2 = input("enter fruit name: ")
fruits.append(f2)
f3 = input("enter fruit name: ")
fruits.append(f3)

print(fruits)


#Write a program to accept marks of 6 students and display them in a sorted manner

Marks=[]
f1 = int(input("enter Marks: "))
Marks.append(f1)
f2 = int(input("enter Marks: "))
Marks.append(f2)
f3 = int(input("enter Marks: "))
Marks.append(f3)
Marks.sort()
print(Marks)

