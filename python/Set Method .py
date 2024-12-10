#-------- difference -----------
a = {1 , 2 , 3 , 4}
b = {"ahmed", 2 , 4 , "ahmed"}
print(a.difference(b))  # a - b

print("="*50) #<< Separator 

#-------difference.ubdat--------
k = {1 , 2 , 3 , 4}
h = {"ahmed", 2 , 4 , "ahmed"}
k.difference_update(h)
print(k)  # k - h

print("="*50) #<< Separator 

#-----intersection------
c = {"A","B","c"}
d = {"c","F","G"}
print(c)
print(c.intersection(d)) # c & d

print("="*50) #<< Separator 

#---intersection-ubdat----------
M = {"A","B","c",5}
R = {"c","F","G",5}
print(M)
M.intersection_update(R) # c & d
print(M)

print("="*50) #<< Separator 

#---------symmetric difference-------
L = {"A","B","c",5}
V = {"c","F","G",5}
print(L)
print(L.symmetric_difference(V))

print("="*50) #<< Separator

#----------------




