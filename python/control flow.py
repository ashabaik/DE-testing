#-----control Flow-----
#--- if , Else , Elif 


YName = input("whts You Name ? ")

CName = input("what your cours need to learn ? ")
UCountry = input("what you cuntry ? ")
Age = input("how old are you ? ")
Cprice = 1500
isstudent = "Yes"
if int(Age) > 24 :
 isstudent = "no"
else : isstudent ="Yes"


if UCountry == "egypt" and isstudent == "Yes" :
 print(f"Hallow {YName} Becuase You from {UCountry} and you are student  you will get cours  for free ")
 print(f"price will be after discount is {Cprice - 1500} $")
elif "egypt" and isstudent == "no" :
 print(f"Hallow {YName} Becuase You from {UCountry} you will get discount abou 50 % ")
 print(f"price will be after discount is {Cprice - 750} $")
elif UCountry == "KSA" :
 print(f"Hallow {YName} Becuase You from {UCountry} you will get discount about 500$")
 print(f"price will be after discount is {Cprice-500} $")
else:  
 print(f"Hallow {YName} Becuase You from {UCountry} You will gat discount 300 $")
 print(f"price will be after discount is {Cprice-300} $")

 print("=="*50)

#-------------------------------------------
MoviRate = 18
print("Movi is not Good For Your Age "if int(Age )< MoviRate else "Move good for your age happi watching")