MyNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in MyNumbers: 
    if number % 2 == 0:
        print(f"{[number]} is even")
    else:
        print(f"{[number]} is odd")
else:
    print("All numbers are checked")
print("=="*50)
#------------------------
MyName = "Shekaa"
for letter in MyName:
    print(f"[ { letter.upper() } ]")

print("=="*50)

    #--------------------------
MySkills = {"HTML":"100%",
            "CSS":"80%",
            "JavaScript":"70%",
            "Python":"90%",
            "Go":"40%",
            }
for skill in MySkills:
    print(f"My progress with {skill} is :{MySkills[skill]}")

    print("=="*50)

    #-------------------------------
    