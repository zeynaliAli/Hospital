from model.user import User


class Patient(User):

    @staticmethod
    def init_db(db):
        sql = """
        CREATE TABLE IF NOT EXISTS patient
        patient_id      int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        user_id         int NOT NULL,
        room            varchar(50) UNIQUE,
        debit           int,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
        """
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.close()
        db.commit()
