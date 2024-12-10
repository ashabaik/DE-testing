#------issuperset------
a = {1,2,3,4,5}
b = {2,4}
c = {2,4,6}
print(a.issuperset(b))  # True 
print(a.issuperset(c))  # False

print("="*50) #<< Separator

#------issupset----------
k = {1,2,3,4,5}
h = {2,4}
g = {2,4,5,1,6,10,3}
print(k.issubset(h))  #False
print(k.issubset(g))  #True

print("="*50) #<< Separator

#---------isdisjoint-------
s = {1,2,3,4,5}
q = {2,4,8,10}
w = {11,16,17,20}
print(s.isdisjoint(q)) #False
print(s.isdisjoint(w)) #True 

print("="*50) #<< Separator

#---------------

