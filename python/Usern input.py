#---User Input------

#FNname = input("what is your first name " )

#MName =  input("what is your middel nam " )

#lname =  input("whate is your laste name ")

#FNname = FNname.capitalize()
#MName = MName.capitalize()
#lname = lname.capitalize()

#print(f"Hallow {FNname} {MName:.1s} {lname} Happy To See You")

#----Practical slice Email---------
email = "ahmed.midooo25@yahoo.com"
print(email[:email.index("@")])

#------------------------
Age = int(input("what is your age ? "))

month   = Age*12
weeks   = month*4
days    = Age*365
mints   = days*60
secound = mints*60

print("You lived For : ")
print(f"{month} Month.",f"{weeks} weeks.",f"{days:,} days.",f"{mints:,}",f"{secound:,} secound")


