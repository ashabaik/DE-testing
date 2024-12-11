from flask import Flask ,render_template


Skill_App = Flask(__name__)
@Skill_App.route("/")
def HomePage():
    return render_template("HomeBage.html")
@Skill_App.route("/about")
def AboutPage():
    return "Hello From AboutPage"
if __name__ == "__main__":
    Skill_App.run(debug=True,port=9000)
    


