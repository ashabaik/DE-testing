import sqlite3

try:
    # الاتصال بقاعدة البيانات
    DB = sqlite3.connect('database.db')
    cr = DB.cursor()

    # إنشاء الجداول إذا لم تكن موجودة
    cr.execute("CREATE TABLE IF NOT EXISTS users (user_id integer, name text)") 
    cr.execute("CREATE TABLE IF NOT EXISTS skills (name text, progress integer, user_id integer)")

    # إدخال بيانات في جدول users
    #cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'Ahmed')")
    #cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'Mohamed')")
    #cr.execute("INSERT INTO users (user_id, name) VALUES (3, 'Yousra')")
    My_Liste = ["Ahmde","Moahmed","Syed","Yousra","ibrahem","fatma"]
    for key,users in enumerate(My_Liste):
        cr.execute(f"INSERT INTO users (user_id, name) VALUES ({key+1}, '{users}')")

    # حفظ التغييرات
    DB.commit()

    #تحديث البيانات 
    cr.execute("UPDATE users SET name = 'Elzero' WHERE user_id = 1")

    #مسح البيانات
    cr.execute("DELETE FROM users WHERE user_id = 1")

    # اختبار البيانات
    cr.execute("SELECT * FROM users")
    #fetchone >>> بتحدد صف واحد فقط من الداتا  :: fetchmany بتحدد عدد الصفوف المحتاج تحددها 
    print(cr.fetchall())

except sqlite3.Error as e:
    print("ُError again:", e)

finally:
    # إغلاق الاتصال بقاعدة البيانات
    DB.close()
