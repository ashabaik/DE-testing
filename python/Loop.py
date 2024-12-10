#---- Loop =  While -----------

Arsnal = []
maxplayers = 5
while maxplayers > 0 :
    players = input("insert one of squad team " )
    Arsnal.append(players)
    maxplayers -= 1
    print(f"player was added ,{maxplayers} player left")
else : 
    print("squad full now")

print(Arsnal)

if len(Arsnal) > 0 : 
    Arsnal.sort()
    index = 0
    while index < len(Arsnal) :
        print(Arsnal[index])
        index += 1 
        print("squad full now")
        #-------------------------