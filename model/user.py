import base64

import MySQLdb


class User:

    def __init__(self,
                 username,
                 password,
                 phone,
                 mail,
                 **kwargs):
        self.id = kwargs.get("id")
        self.username = username
        self.password = password
        self.phone = phone
        self.mail = mail
        self.address = kwargs.get("address", None)
        self.postal_code = kwargs.get("postal_code", None)
        self.birthday = kwargs.get("birthday", None)
        self.age = kwargs.get("age", None)
        self.gender = kwargs.get("gender", None)
        self.height = kwargs.get("height", None)
        self.weight = kwargs.get("weight", None)

    def save(self, db, role):
        sql_create = """
         CREATE TABLE IF NOT EXISTS user
         (pid        int NOT NULL AUTO_INCREMENT UNIQUE,
         username    varchar(50) NOT NULL UNIQUE,
         password    varchar(50) NOT NULL,
         phone       varchar(50) NOT NULL UNIQUE,
         mail        varchar(50) NOT NULL UNIQUE,
         role        varchar(50) NOT NULL,
         uuid        varchar(50) NOT NULL UNIQUE,
         address     varchar(150),
         postal_code varchar(10),
         birthday    bigint,
         age         int,
         gender      varchar(10),
         height      int,
         weight      int);
         """

        sql_insert = """
         INSERT INTO user
         (username, password, phone, mail, role, uuid, address, postal_code, birthday, age, gender, height, weight)
         VALUES
         (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
         """
        uuid = base64.b64encode(bytes(role + "--" + self.mail, 'utf-8')).decode('utf-8')

        val = (self.username,
               self.password,
               self.phone,
               self.mail,
               role,
               uuid,
               self.address,
               self.postal_code,
               self.birthday,
               self.age,
               self.gender,
               self.height,
               self.weight)

        cursor = db.cursor()
        cursor.execute(sql_create)
        cursor.execute(sql_insert, val)
        cursor.close()
        db.commit()

        return uuid

    @staticmethod
    def load(uuid, password, db):

        sql = """
        SELECT * FROM user
        WHERE uuid = %s AND password = %s
        """

        cursor = db.cursor()
        cursor.execute(sql, (uuid, password))
        record = cursor.fetchone()
        cursor.close()

        user = User(record[1],
                    record[2],
                    record[3],
                    record[4],
                    address=record[5],
                    postal_code=record[6],
                    birthday=record[7],
                    age=record[8],
                    gender=record[9],
                    height=record[10],
                    weight=record[11],
                    id=record[0])
        print(record)
        print(user.height)
        return user

    @staticmethod
    def update(db, user_id, **kwargs):
        cursor = db.cursor()
        for key in kwargs.keys():
            sql = "UPDATE user SET " + key + "= %s WHERE pid = %s"
            print(key)
            print(kwargs.get(key))
            cursor.execute(sql, (kwargs.get(key), user_id))
        cursor.close()
        db.commit()
