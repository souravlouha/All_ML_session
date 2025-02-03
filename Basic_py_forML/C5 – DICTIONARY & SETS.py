
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




