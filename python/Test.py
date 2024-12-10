admin = ["ahmed","moahmed","syed","shabaik"]
print(admin)
name  = input("what is you name ? " )
if name in admin:
 print(f"Welcom bakck {name}")
 opthin = input("you need to updat your data ubdat now or delet ? ")
 if opthin == "ubdat" : 
      newname = input("what is your new name ? " )
      print(f"your data is ubdated now new name is {newname} .")
      admin[admin.index(name)]=newname
      print(admin)
 elif opthin == "delet":
   print("yore data was delted now")
   admin.remove(name)
   print(admin)
 else :
   print("no opthion for this ")
else : 
   stsus = input("you not admin you cant open this website you wanted to add yes or no ? ")
   if stsus == "Yes" :
      print("you are added now can open the wepsite")
      admin.append(name)
      print(admin)
   else: 
      print("wepsite closed until you be from admin")



    

