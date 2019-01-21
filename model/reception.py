from model.user import User


class Reception(User):

    @staticmethod
    def init_db(db):
        timetable_sql = """
        CREATE TABLE IF NOT EXISTS timetable
        (timetable_id     int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        doctor_id         int NOT NULL,
        patient_id        int,
        visit_date        datetime,
        accepted          boolean,
        emergency         boolean,
        room              varchar(50) UNIQUE,
        description       text,
        FOREIGN KEY (doctor_id) REFERENCES user(user_id),
        FOREIGN KEY (patient_id) REFERENCES user(user_id))
        """
        cursor = db.cursor()
        cursor.execute(timetable_sql)
        cursor.close()
        db.commit()