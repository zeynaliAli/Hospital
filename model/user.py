import base64


class User:

    def __init__(self,
                 username,
                 password,
                 phone,
                 mail,
                 role_id,
                 **kwargs):
        self.id = kwargs.get("id")
        self.username = username
        self.password = password
        self.phone = phone
        self.mail = mail
        self.role_id = role_id
        self.address = kwargs.get("address", None)
        self.postal_code = kwargs.get("postal_code", None)
        self.birthday = kwargs.get("birthday", None)
        self.age = kwargs.get("age", None)
        self.gender = kwargs.get("gender", None)
        self.height = kwargs.get("height", None)
        self.weight = kwargs.get("weight", None)

    @staticmethod
    def init_db(db):
        sql_create = """
                 CREATE TABLE IF NOT EXISTS user
                 (user_id    int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
                 username    varchar(50) NOT NULL UNIQUE,
                 password    varchar(50) NOT NULL,
                 phone       varchar(50) NOT NULL UNIQUE,
                 mail        varchar(50) NOT NULL UNIQUE,
                 role_id     int NOT NULL,
                 uuid        varchar(50) NOT NULL UNIQUE,
                 address     varchar(150),
                 postal_code varchar(10),
                 birthday    bigint,
                 age         int,
                 gender      varchar(10),
                 height      int,
                 weight      int);
                 """
        cursor = db.cursor()
        cursor.execute(sql_create)
        cursor.close()
        db.commit()

    def save(self, db):
        sql_insert = """
         INSERT INTO user
         (username, password, phone, mail, role_id, uuid, address, postal_code, birthday, age, gender, height, weight)
         VALUES
         (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
         """
        uuid = base64.b64encode(bytes(self.role_id + "--" + self.mail, 'utf-8')).decode('utf-8')
        val = (self.username,
               self.password,
               self.phone,
               self.mail,
               self.role_id,
               uuid,
               self.address,
               self.postal_code,
               self.birthday,
               self.age,
               self.gender,
               self.height,
               self.weight)
        cursor = db.cursor()
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
                    record[5],
                    address=record[7],
                    postal_code=record[8],
                    birthday=record[9],
                    age=record[10],
                    gender=record[11],
                    height=record[12],
                    weight=record[13],
                    id=record[0])
        return user

    @staticmethod
    def update(db, user_id, **kwargs):
        cursor = db.cursor()
        for key in kwargs.keys():
            sql = "UPDATE user SET " + key + "= %s WHERE user_id = %s"
            cursor.execute(sql, (kwargs.get(key), user_id))
        cursor.close()
        db.commit()

    def edit_profile(self, db):
        address = input("Enter you address. [Enter to skip or keep current]")
        postal_code = input("Enter you postal code. [Enter to skip or keep current]")
        birthday = input("Enter you birthday. [Enter to skip or keep current]")
        age = input("Enter you age. [Enter to skip or keep current]")
        gender = input("Enter you gender. [Enter to skip or keep current]")
        height = input("Enter you height. [Enter to skip or keep current]")
        weight = input("Enter you weight. [Enter to skip or keep current]")
        User.update(db,
                    self.id,
                    address=address,
                    postal_code=postal_code,
                    birthday=birthday,
                    age=age,
                    gender=gender,
                    height=height,
                    weight=weight)

    def show_menu(self, db):
        print("0 - edit profile")
