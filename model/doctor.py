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

    def show_schedule(self):
        return

    def show_menu(self, db):
        super().show_menu(db)
        print("1 - show schedule")
        print("2 - send PM to a patient")
        print("3 - cancel an appointment")
        choice = int(input())
        if choice == 1:
            self.show_schedule()
        elif choice == 2:
            self.send_pm()
        elif choice == 3:
            self.cancel_appointment()
