MySkills = {
  "Css": "70%",
  "Python": "90%",
  "C++": "80%"
}
myTubel = ("HTML", "go", "JS")
def ShowSkills (name,*Skills,**SkillsWithProgress):

  print(f"Hallow {name} Your Skills with Out Progress Is : ") 
  for skill in Skills:
    print(f"- {skill}")
  print("Your Skills With Progress Is : ")
  for Skill_Key , Skill_Value in SkillsWithProgress.items():
    print(f"> {Skill_Key} => {Skill_Value} ")

ShowSkills("Ahmed",*myTubel,**MySkills)
print("=="*60)
def cleanword(word):
    if len(word) == 1:
        return word
    elif word[0] == word[1]:
        return cleanword(word[1:])
    return word[0] + cleanword(word[1:])
    #---------------------------
print(cleanword("PPEEPPOOLL"))
print("=="*60)
print("=="*60)
print("=="*60)
#-----------------------------
import os
print(os.getcwd())    # Main Current Directory
print(os.path.dirname(os.path.abspath(__file__)))  #  Directory for the open File
file = open("D:\DATA\python\Ahmed.txt")