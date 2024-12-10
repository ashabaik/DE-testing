import sqlite3

# Establish connection to the database and create a cursor object
db = sqlite3.connect("app.db")
cr = db.cursor()

# Create the skills table if it doesn't exist
cr.execute("""
CREATE TABLE IF NOT EXISTS skills (
    skill_id INTEGER PRIMARY KEY,
    name TEXT,
    progress INTEGER
)
""")


# Ahmed Mohamed 

def commit_and_close():
    """Commit changes and close the database connection"""
    db.commit()
    db.close()
    print("Connection to Database is Closed")

# Message to prompt the user for their choice
input_message = """
What do you want to do?
"A" => Add new skill
"D" => Delete skill
"U" => Update skill
"S" => Search skill
"Q" => Quit the app
Choose option: """

commands_list = ["A", "D", "U", "S", "Q"]

def add_new_skill():
    """Add a new skill"""
    skill_id = input("Enter skill ID: ").strip()
    name = input("Enter skill name: ").strip()
    
    # Check if the skill name already exists in the database
    cr.execute("SELECT * FROM skills WHERE name = ?", (name,))
    existing_skill = cr.fetchone()
    
    if existing_skill:
        print(f"Error: Skill with the name '{name}' already exists.")
    else:
        progress = input("Enter skill progress (0-100): ").strip()
        try:
            cr.execute("INSERT INTO skills (skill_id, name, progress) VALUES (?, ?, ?)", (skill_id, name, progress))
            print(f"Skill {name} with progress {progress}% added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Skill ID already exists.")
    commit_and_close()

def delete_skill():
    """Delete a skill"""
    skill_id = input("Enter skill ID to delete: ").strip()
    cr.execute("DELETE FROM skills WHERE skill_id = ?", (skill_id,))
    if cr.rowcount > 0:
        print(f"Skill with ID {skill_id} deleted successfully.")
    else:
        print(f"No skill found with ID {skill_id}.")
    commit_and_close()

def update_skill():
    """Update skill information"""
    skill_id = input("Enter skill ID to update: ").strip()
    new_name = input("Enter new skill name: ").strip()
    new_progress = input("Enter new progress (0-100): ").strip()
    cr.execute("UPDATE skills SET name = ?, progress = ? WHERE skill_id = ?", (new_name, new_progress, skill_id))
    if cr.rowcount > 0:
        print(f"Skill with ID {skill_id} updated successfully.")
    else:
        print(f"No skill found with ID {skill_id}.")
    commit_and_close()

def search_skill():
    """Search for a skill"""
    skill_id = input("Enter skill ID to search: ").strip()
    cr.execute("SELECT * FROM skills WHERE skill_id = ?", (skill_id,))
    skill = cr.fetchone()
    if skill:
        print(f"Skill found: ID = {skill[0]}, Name = {skill[1]}, Progress = {skill[2]}%")
    else:
        print(f"No skill found with ID {skill_id}.")
    commit_and_close()

def quit_the_app():
    """Quit the application"""
    print("Quit the app")
    commit_and_close()

# Call functions based on user input
user_input = input(input_message).strip().upper()

if user_input in commands_list:
    if user_input == "A":
        add_new_skill()
    elif user_input == "D":
        delete_skill()
    elif user_input == "U":
        update_skill()
    elif user_input == "S":
        search_skill()
    elif user_input == "Q":
        quit_the_app()
else:
    print("Sorry, this command not found.")
    print("Please choose one of the following")
