import MySQLdb

from model import user
from model.user import User
from utils.mail_util import send_mail_to

db = MySQLdb.connect("localhost", "root", "suchadream", charset='utf8', use_unicode=True)


def create_db():
    sql = "CREATE DATABASE IF NOT EXISTS hospital DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
    sql_use = "USE hospital;"
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.execute(sql_use)
    cursor.close()
    db.commit()


def register():
    # u = User("alizeyn1", "suchadream1", "092118457971", "ali.zzeynali@gmail.org")
    # uuid = u.save(db, "Doctor")

    username = input("Enter your username :")
    password = input("Enter your password :")
    phone = input("Enter your phone number :")
    mail = input("Enter your mail :")
    role_id = input("""
    Enter your role :
    1 - Doctor
    2 - Nurse
    3 - Lab
    4 - Pharmacy
    5 - Patient
    6 - Accounting
    7 - Reception
    """)
    u = User(username, password, phone, mail, role_id)
    uuid = u.save(db)
    print("Your registration has been successful, check you mail for uuid.")
    send_mail_to(u.mail, """
        Your registration has been successful.
        Your login id is : {}
    """.format(uuid))


def login():
    return


def reset_pass():
    mail = input("enter your email\n")
    print(mail)
    sql = """
    SELECT * FROM user
    WHERE mail = %s
    """
    cursor = db.cursor()
    cursor.execute(sql, (mail,))
    row = cursor.fetchone()
    print(row)
    cursor.close()
    if row is not None:
        send_mail_to(mail, """
    Your uuid is {} 
    Your password is {}
    Don't forget it again.
    """.format(row[2], row[6]))


def main():
    create_db()
    # register(db, "Doctora")
    # User.load("RG9jdG9yYS0tYWxpLnp6ZXluYWxpQGdtYWlsLm9yZw==", "suchadream1", db)
    # User.update(db, 3, address="fallahi", age=22)
    print("""
    0 - Login
    1 - Register
    2 - Forgot Password
    """)
    choice = int(input())
    if choice == 0:
        login()
    elif choice == 1:
        register()
    elif choice == 2:
        reset_pass()
    print(choice)


main()
