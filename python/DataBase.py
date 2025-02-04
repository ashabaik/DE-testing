import sqlite3

try:
    # Connect to the SQLite database (it will create the database if it doesn't exist)
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()

        # Create tables if they do not exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT)") 
        cursor.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

        # Insert data into the users table
        user_names = ["Ahmed", "Mohamed", "Syed", "Yousra", "Ibrahem", "Fatma"]
        for index, name in enumerate(user_names):
            cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", (index + 1, name))

        # Commit the changes to the database
        connection.commit()

        # Update a specific user's name in the users table
        cursor.execute("UPDATE users SET name = 'Elzero' WHERE user_id = 1")

        # Delete a user from the users table
        cursor.execute("DELETE FROM users WHERE user_id = 1")

        # Retrieve and display all users
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)

except sqlite3.Error as error:
    print("An error occurred:", error)

