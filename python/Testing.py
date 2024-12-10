#set Method

#---------clear ---------------
a = {1,2,3,4,5}
a.clear() 
print(a)
#---------Union------------------
b = {3,6,9,12}
c = {2,4,8,10}
print(b.union(c)) 
#---------Add-----------------------
x = {5,15,20}
x.add(25)
print(x)
#--------Copy-------------------------
e = {20,30,40}
f = e.copy()
print(e)
print(f)
#---------remove------------#discard make smae but dont get eror 
g = {1,2,3,4}
g.remove(2)
print(g)
#--------------Ubdat------------
h = {"ahmed","Mohamed","khaled"}
k = {"yousra","ahmed","ibrahem","Mohamed",100}
h.update(k)
print(h)
#---------------

 