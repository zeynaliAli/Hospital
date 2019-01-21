from model.user import User


class Doctor(User):

    @staticmethod
    def init_db(db):

        private_message_sql = """
        CREATE TABLE IF NOT EXISTS pm 
        (pm_id             int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        timetable_id       int NOT NULL,
        doctor_id          int NOT NULL,
        patient_id         int NOT NULL,
        pm                 text NOT NULL,
        FOREIGN KEY (doctor_id)  REFERENCES user(user_id),
        FOREIGN KEY (patient_id) REFERENCES user(user_id))
        """

        prescription_sql = """
        CREATE TABLE IF NOT EXISTS prescription
        (prescription_id   int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        doctor_id          int NOT NULL,
        patient_id         int NOT NULL,
        description        text,
        FOREIGN KEY (doctor_id)  REFERENCES user(user_id),
        FOREIGN KEY (patient_id) REFERENCES user(user_id))
        """

        cursor = db.cursor()
        cursor.execute(private_message_sql)
        cursor.execute(prescription_sql)
        cursor.close()
        db.commit()

    def cancel_appointment(self):
        return

    def send_pm(self):
        return

    def show_schedule(self, db):
        sql = """
        SELECT * FROM timetable
        WHERE doctor_id = %s
        """

        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        for row in rows:
            time = row[3]
            accept = "---" if row[4] is None else row[4]
            sql = """
            SELECT username, mail 
            FROM user 
            INNER JOIN timetable ON user.user_id = timetable.patient_id
            WHERE timetable.visit_date = %s
            """
            cursor.execute(sql, (time,))
            patient = cursor.fetchone()
            patient = patient if patient is not None else "---"
            print("Time: {}\t Patient: {}\t Accept Status: {}\t".format(time, patient, accept))

        cursor.close()
        db.commit()
        return

    def add_visit_time(self, db):
        date = input("Enter your time (example : 2019-06-13 13:10) : \n")
        sql = """
        INSERT INTO timetable
        (doctor_id, visit_date)
        VALUES
        (%s, %s)
        """
        cursor = db.cursor()
        cursor.execute(sql, (self.id, date))
        cursor.close()
        db.commit()
        print("Done!")
        self.show_menu(db)
        return

    def show_menu(self, db):
        super().show_menu(db)
        print("1 - show schedule")
        print("2 - send PM to a patient")
        print("3 - cancel an appointment")
        print("4 - Add free time to visit")
        choice = int(input())
        if choice == 1:
            self.show_schedule(db)
        elif choice == 2:
            self.send_pm(db)
        elif choice == 3:
            self.cancel_appointment(db)
        elif choice == 4:
            self.add_visit_time(db)
