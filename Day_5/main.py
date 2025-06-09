# List data structure built-in functions use cases

a = [1,2,3,3,4,5,True,"abc"]

a.append(5) # Appends 5 at the end of the list
print(a)

b = a.copy() # Creates another copy of list a

print(a.count(3)) # counts the number of element in the list

a.extend([1,2,3]) #Extends the list by given list
print(a)

print(a.index(3)) #Returns the index of first occurrence of element

a.insert(0,5) # Insert index 0 element 5
print(a)

a.pop(5) # Removes the last occurrence of element
print(a)

a.remove(5) #Removes the first occurrence of element
print(a)

a.reverse() #Reverse the list
print(a)

c = [2,5,3,1,4]
c.sort() #sort the list
print(c)

a.clear()#Clears the list
print(a)

