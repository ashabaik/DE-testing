YourPassword = input("enter your password: ")
password  = "Shekaa1996"
tris = 3  
if YourPassword == password :
            print("welcome back to your account")  
while YourPassword != password :
    if tris > 0 :
        YourPassword = input("worng passowrd try again: ")
        tris -= 1
        print(f"you have {tris} tris left")
    else :
        print("try again later")
        break   