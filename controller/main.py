import MySQLdb

from model import user
from model.accounting import Accounting
from model.doctor import Doctor
from model.lab import Lab
from model.patient import Patient
from model.pharmacy import Pharmacy
from model.reception import Reception
from model.user import User
from utils.mail_util import send_mail_to

db = MySQLdb.connect("localhost", "root", "suchadream", charset='utf8', use_unicode=True)
login_user = None


def init_db():
    sql = "CREATE DATABASE IF NOT EXISTS hospital DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
    sql_use = "USE hospital;"
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.execute(sql_use)
    cursor.close()
    db.commit()

    User.init_db(db)
    Doctor.init_db(db)
    Lab.init_db(db)
    Pharmacy.init_db(db)
    Patient.init_db(db)
    Reception.init_db(db)
    Accounting.init_db(db)


def register():
    username = input("Enter your username :")
    password = input("Enter your password :")
    phone = input("Enter your phone number :")
    mail = input("Enter your mail :")
    role_id = input("""
    Enter your role :
    1 - Doctor
    2 - Lab
    3 - Pharmacy
    4 - Patient
    5 - Accounting
    6 - Reception
    """)
    u = User(username, password, phone, mail, role_id)
    uuid = u.save(db)
    print("Your registration has been successful, check you mail for uuid.")
    send_mail_to(u.mail, """
        Your registration has been successful.
        Your login id is : {}
    """.format(uuid))


def login():
    global login_user
    uuid = input("Enter UUID: ")
    sql = "SELECT * FROM user WHERE uuid = %s"
    cursor = db.cursor()
    cursor.execute(sql, (uuid,))
    row = cursor.fetchone()
    if row is not None:
        password = input("Enter your password: ")
        sql = "SELECT * FROM user WHERE password = %s"
        cursor.execute(sql, (password,))
        row = cursor.fetchone()
        if row is not None:
            login_user = User.load(uuid, password, db)
            login_user = change_to_role(login_user)
            print("login user mail is " + login_user.mail)
            login_user.show_menu(db)


def change_to_role(user):
    role_id = user.role_id
    if role_id == 1:
        user.__class__ = Doctor
    elif role_id == 2:
        user.__class__ = Lab
    elif role_id == 3:
        user.__class__ = Pharmacy
    elif role_id == 4:
        user.__class__ = Patient
    elif role_id == 5:
        user.__class__ = Accounting
    elif role_id == 6:
        user.__class__ = Reception

    return user


def reset_pass():
    mail = input("enter your email\n")
    sql = """
    SELECT * FROM user
    WHERE mail = %s
    """
    cursor = db.cursor()
    cursor.execute(sql, (mail,))
    row = cursor.fetchone()
    cursor.close()
    if row is not None:
        send_mail_to(mail, """
    Your uuid is {} 
    Your password is {}
    Don't forget it again.
    """.format(row[2], row[6]))


def main():
    init_db()
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
    # elif choice == 3:


main()
