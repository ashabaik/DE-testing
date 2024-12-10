print("Ahmed mohamed") #this all for test 
print (type(100))
print (type(1.5))
print (type("ahmed"))
Name ="Ahmed Mohamed"
print(Name)
#-----------------------
help("keywords")
a,b,c = 1,2,3
print(a,b,c)
print(a)
print(b)
print(c)
#------------------------
#strip()r,l >> To Delat all space
#title
a = "Ahmed mohamed elsyed"
print(a.title())
#----------------------
#count
b = "ahmed moahmed ahmed ibrahim khaled ahmed" 
print (b.count("ahmed")) # he collect  number of ahmed 
#--------------------
#startswith // endswith
k = "i love mohamed my son"
print(k.startswith("i"))
print(k.startswith("m"))
print(k.startswith("m",7,15))
#-----------------------------
#find or index 
f = "i love my girle yousra"
print(f.index("y"))
print(f.find("y"))
#------------------
# replace (old value,new value , count)
z = "go to my room for one tow one tow one tow "
print(z.replace("one","1"))
print(z.replace("one","1",2))
#-------------------------
# join
n = ["ahmed","moahmed","shabaik"]
print("-".join(n))
#-----------------------
name = "Ahmed"
age = 29 
degree = 10.5
print("My Name Is : %s"%name)
print("My Name Is : %s and My Age is : %d"%(name,age))
print("My Name Is : %s and My Age is : %d and My degree is : %f"%(name,age,degree))
# %s= string ,, %d = number,,,  %f = folting number 
#----------------------------------------------------------------------------
# Arithmetic Operators 
# [+]  Addition 
# [-]  Subtraction 
# [*]  Multiplicathion 
# [/]  Division 
# [%]  Modulus
# [**] Exponet
# [//] Floor Division 
#---------Ex---------------
print(10+20) # = 30   Addition
print(50-30) # = 20   Subtraction
print(5*5)   # = 25   Multiplicathion
print(50/5)  # = 10.0 Division
print(50%5)  # = 0    Modulus
print(2**5)  # = 32   Exponet
print(50//5) # = 10   Floor Division
#------------------------------------------------------------------
# List []  -----------
MyList = ["Name","Age","Degre","ID","Adress"]
print(MyList)
print(MyList[1:3]) # Age = 1 , Degere = 2 
#(append) to add eliment in your list 
MyList.append("Ahmed")
print(MyList)
#(extend)
a = [1,2,3,4]
b = ["one","tow","three","four"]
a.extend(b)
print(a)
# (remove) to remove elemint from list
x = ["ahmed","mohamed","khaled"]
x.remove("khaled")
print(x)
# Sort 
y = [1,5,3,7,22,120,10,9]
y.sort(reverse=True)
print(y)
u = [1,5,3,7,22,120,10,9]
u.sort()
print(u)
# reverse()
z = [100,50,200,150,"ahmed",30]
z.reverse()
print(z)
# Clere() delet all elmint from list
f = [1,2,3]
f.clear()
print(f)
#--------------
