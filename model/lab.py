from model.user import User


class Lab(User):

    @staticmethod
    def init_db(db):

        test_sql = """
        CREATE TABLE IF NOT EXISTS test
        (test_id          int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        lab_id            int NOT NULL,
        doctor_id         int NOT NULL,
        patient_id        int NOT NULL,
        description       text,
        price             int,
        FOREIGN KEY (lab_id)        REFERENCES user(user_id),
        FOREIGN KEY (doctor_id)     REFERENCES user(user_id),
        FOREIGN KEY (patient_id)    REFERENCES user(user_id))
        """

        cursor = db.cursor()
        cursor.execute(test_sql)
        cursor.close()
        db.commit()
