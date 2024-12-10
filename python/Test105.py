class member :
    def __init__(self,Fname,Mname,Lname,Grender) :
        self.FistName = Fname
        self.MiddleName = Mname
        self.LastName = Lname
        self.Gender = Grender
    def FulName(self) :
        return f"{self.FistName} {self.MiddleName} {self.LastName}"
    
    def Hello(self) :
        if self.Gender == "Male" :
            return f"Hello Mr {self.FistName}"
        elif self.Gender == "Female" :
            return f"Hello Miss {self.FistName}"
        else :
            return f"Hello {self.FistName}"
member_one = member("Ahmed", "Elsayed", "Mohamed", "Male")
member_two = member("Sara", "Elsayed", "Ali", "Female")
member_three =member("ibrahim", "Elsayed", "Ali", "Male")
print(member_one.Hello())