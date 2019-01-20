import MySQLdb
import base64
from model.user import User


def insert_user(db, user, role):
    sql_create = """
    CREATE TABLE IF NOT EXISTS user
    (pid        int NOT NULL AUTO_INCREMENT UNIQUE,
    username    varchar(50) NOT NULL UNIQUE,
    password    varchar(50) NOT NULL,
    phone       varchar(50) NOT NULL UNIQUE,
    mail        varchar(50) NOT NULL UNIQUE,
    role        varchar(50) NOT NULL UNIQUE,
    uuid        varchar(50) NOT NULL UNIQUE,
    address     varchar(150),
    postal_code varchar(10),
    birthday    bigint,
    age         int,
    gender      varchar(10),
    height      int,
    weight      int);
    """

    # sql_create = "drop table user;"

    sql_insert = """
    INSERT INTO user
    (username, password, phone, mail, role, uuid, address, postal_code, birthday, age, gender, height, weight)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    uuid = base64.b64encode(bytes(role + "--" + user.mail, 'utf-8')).decode('utf-8')
    print(uuid)
    val = (user.username,
           user.password,
           user.phone,
           user.mail,
           role,
           uuid,
           user.address,
           user.postal_code,
           user.birthday,
           user.age,
           user.gender,
           user.height,
           user.weight)

    cursor = db.cursor()
    cursor.execute(sql_create)
    cursor.execute(sql_insert, val)
    cursor.close()
    db.commit()

    return uuid

# todo update user
