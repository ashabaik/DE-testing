def MyDecrator (func) : 
    def wrapper (*N) :
        for number in N:
     
         if number < 0:
            print("the number is less than 0")
        func(*N)
    return wrapper
#--------------------
@MyDecrator
def calculator (n1, n2,n3,n4) :
    print(n1 + n2 + n3 - n4)
calculator(-10,20,50,30)
   
      