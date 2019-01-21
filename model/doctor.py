from model.user import User


class Doctor(User):

    @staticmethod
    def init_db(db):
        sql = """
        CREATE TABLE IF NOT EXISTS timetable
        timetable_id      int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        doctor_id         int NOT NULL,
        time              datetime,
        requested_by      int,
        accepted          boolean,
        emergency         boolean,
        FOREIGN KEY (doctor_id) REFERENCES user(user_id),
        FOREIGN KEY (requested_by) REFERENCES user(user_id)
        """
        cursor = db.cursor()
        cursor.execute(sql)
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
