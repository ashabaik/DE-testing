#---Dictionary----------
User = { "Name" : "Ahmed",
        "Age" : 35 , 
        "country" : "Egypet",
        "Skils" : ("Html","css","PHP"),
        "rating": 10.5
}
print(User)
print(User.get("Name"))
print(User.keys())
print(User.values())

print("=="*40) # sepratore 

#------Tow-Dimensional Dictionary-----
Data = {"one" : {"name":"Ahmed","Age" : 29},
        "tow": {"name": "Yousra","Age":26},
        "three": {"name": "Mohamed","Age": 2}
        }
print(Data)
print(Data["three"]["name"])
print(len(Data))

print("=="*40) # sepratore

#----------------------

member = {"skill":"HTML","Time":"5H"}
print(member)
member.update({"Degree":"80%"})
print(member.popitem())

print("=="*40) # sepratore

#------fromkeys-------

a = ("Ahmed","Moahmed","Yousra")
b = ("Family")
print(dict.fromkeys(a,b))

print("=="*40) # sepratore

