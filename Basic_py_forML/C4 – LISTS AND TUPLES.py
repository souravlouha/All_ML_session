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

###Write a program to store three fruits in a list entered by the user.
fruits=[]
f1 = input("enter fruit name: ")
fruits.append(f1)
f2 = input("enter fruit name: ")
fruits.append(f2)
f3 = input("enter fruit name: ")
fruits.append(f3)

print(fruits)


###Write a program to accept marks of 6 students and display them in a sorted manner

Marks=[]
f1 = int(input("enter Marks: "))
Marks.append(f1)
f2 = int(input("enter Marks: "))
Marks.append(f2)
f3 = int(input("enter Marks: "))
Marks.append(f3)
Marks.sort()
print(Marks)


###Check that a tuple type cannot be changed in python?

#Tuples are immutable, meaning once created, their elements cannot be modified.
# Create a tuple
my_tuple = (1, 2, 3)

# Try to change an element
my_tuple[0] = 10
#TypeError: 'tuple' object does not support item assignment
#The line my_tuple[0] = 10 tries to change the first element of the tuple, which is not allowed.
#This simple example proves that tuples cannot be changed in Python. If you need to modify data, use a list instead. For example:
my_list = [1, 2, 3]
my_list[0] = 10  # This works fine
print(my_list)   # Output: [10, 2, 3]



###Write a program to sum a list with 4 numbers.
a= [1, 2, 3]
print(sum(a))  # Output: 6



###Write a program to count the number of zeros in the following tuple: p = (7, 0, 8, 0, 0, 9)

p=[7,0 ,8 ,0 ,0 ,9]
n = p.count(0) # Number
print(n) # Output:

