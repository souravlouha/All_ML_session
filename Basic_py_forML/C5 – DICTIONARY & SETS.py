
# DICTIONARY
#Dictionary is a collection of keys-value pairs.
'''
PROPERTIES OF PYTHON DICTIONARIES
1.It is unordered.
2.It is mutable.
3.It is indexed.
4.Cannot contain duplicate keys.
'''
marks = {
  "sourav": 80,
  "soumo":90,
  "bose":70
}
print(marks, type(marks)) #its shows 'dict ' it means dictionary class 

print(marks.keys())

print(marks.values())

print(marks.items()) #returns list of tuples

marks.update({"sourav":45}) #updating value
print(marks)



'''
• a.items(): Returns a list of (key,value)tuples.
• a.keys(): Returns a list containing dictionary's keys.
• a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
• a.get("name"): Returns the value of the specified keys (and value is returned eg."harry" is returned here).
'''

print(marks.get("sumi")) 
print(marks.get("sourav")) #returns value of given key

'''
# difference between (marks.get("sourav")) and (marks["sourav"])

***
(marks.get("sourav2")) #print None
(marks["sourav2"]) #Return an Error 
'''
d = {} # empty dictionary



#SETS



s = {1,2,3} 

e = set()#empty set
#Dont use s ={} as it will creat an empty dictionary

p = {1,4,4,8,6,3,7,5,7} # set a elements repeat hoy na 
print(p) #{1, 3, 4, 5, 6, 7, 8}


# SET METHODS

q = {1, 3, 4, 5, 6, 7, 8, "sourav"} 
print(q,type(q))#<class 'set'>


q.add(9)#add element to set
print(q ,type(q)) 