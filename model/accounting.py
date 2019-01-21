from model.user import User


class Accounting(User):

    @staticmethod
    def init_db(db):
        sql = """
        CREATE TABLE IF NOT EXISTS factor (
        factor_id             int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        patient_id            int NOT NULL,
        price                 int,
        payed                 int,
        description           text,
        FOREIGN KEY (patient_id) REFERENCES user(user_id)
        )
        """
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.close()
        db.commit()