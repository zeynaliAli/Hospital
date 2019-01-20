import MySQLdb

from controller.login import insert_user
from model import user
from model.user import User
from utils.mail_util import send_mail_to


def create_db(db):
    sql = "CREATE DATABASE IF NOT EXISTS hospital DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
    sql_use = "USE hospital;"
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.execute(sql_use)
    cursor.close()
    db.commit()


def register(db, role):
    u = User("alizeyn1", "suchadream1", "092118457971", "ali.zzeynali@gmail.org")
    uuid = insert_user(db, u, role)
    send_mail_to(u.mail, """
        Your registration has been successful.
        Your login id is : {}
    """.format(uuid))


def main():
    db = MySQLdb.connect("localhost", "root", "suchadream", charset='utf8', use_unicode=True)
    create_db(db)
    # register(db, "Doctora")
    # User.load("RG9jdG9yYS0tYWxpLnp6ZXluYWxpQGdtYWlsLm9yZw==", "suchadream1", db)
    User.update(db, 3, address="fallahi", age=22)


main()
