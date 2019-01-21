from smtplib import SMTPRecipientsRefused

from model.user import User
from utils.mail_util import send_mail_to


class Doctor(User):

    @staticmethod
    def init_db(db):

        private_message_sql = """
        CREATE TABLE IF NOT EXISTS pm 
        (pm_id             int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
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

    def cancel_appointment(self, db):
        sql = """
               SELECT u.user_id, u.username, u.mail, t.visit_date
               FROM user u
               INNER JOIN timetable t ON u.user_id = t.patient_id
               WHERE t.doctor_id = %s AND t.accepted = true
               """

        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        for row in rows:
            time = row[3]
            print("""
            Time: {}
            Patient: id = {}, username = {}, email = {}
            Accept Status: {}
            _________________________________________
            """.format(time, row[0], row[1], row[2], row == 1))

        if len(rows) < 1:
            print("There is no any accepted appointment !")
            self.show_menu(db)
            return

        cancel_id = int(input("Enter id of patient you want to cancel the appointment of : \n"))
        sql = """
        UPDATE timetable SET accepted = false
        WHERE patient_id = %s
        """
        cursor.execute(sql, (cancel_id,))
        cursor.close()
        db.commit()
        for row in rows:
                if row[0] == cancel_id:
                    mail = row[2]
                    try:
                        send_mail_to(mail, """
                        Your appointment has been Canceled!
                        """)
                    except SMTPRecipientsRefused:
                        print("Error in sending mail, Address is not valid ")

        self.show_menu(db)
        return

    def accept_appointment(self, db):
        sql = """
               SELECT u.user_id, u.username, u.mail, t.visit_date
               FROM user u
               INNER JOIN timetable t ON u.user_id = t.patient_id
               WHERE t.doctor_id = %s AND (t.accepted = false OR t.accepted is NULL)
               """

        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        for row in rows:
            time = row[3]
            print("""
            Time: {}
            Patient: id = {}, username = {}, email = {}
            Accept Status: {}
            _________________________________________
            """.format(time, row[0], row[1], row[2], row == 1))

        if len(rows) < 1:
            print("There is no any unaccepted appointment !")
            self.show_menu(db)
            return

        accept_id = int(input("Enter id of patient you want to accept the appointment of : \n"))
        sql = """
        UPDATE timetable SET accepted = true
        WHERE patient_id = %s
        """
        cursor.execute(sql, (accept_id,))
        cursor.close()
        db.commit()
        print("Done !")
        self.show_menu(db)
        return

    def send_pm(self, db):
        sql = """
                SELECT user_id, username, mail 
                FROM user 
                INNER JOIN timetable ON user.user_id = timetable.patient_id
                WHERE timetable.doctor_id = %s
                """
        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()

        for row in rows:
            print("""
                    Patient: id = {}, username = {}, email = {}
                    _________________________________________
                    """.format(row[0], row[1], row[2]))

        if len(rows) < 1:
            print("You don't have any patient loser!")
            return

        patient_id = int(input("Enter id of patient you want ot send him/her a pm : \n"))
        msg = input("Type your message : \n")

        sql_save_pm = """
        INSERT INTO pm
        (doctor_id, patient_id, pm)
        VALUES
        (%s, %s, %s)
        """
        cursor.execute(sql_save_pm, (self.id, patient_id, msg))
        print("PM send successfully!")
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

            print("""
            Time: {}
            Patient: {}
            Accept Status: {}
            ________________________________________
            """.format(time, patient, accept == 1))

        cursor.close()
        db.commit()
        self.show_menu(db)
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
        print("4 - accept an appointment")
        print("5 - Add free time to visit")
        choice = int(input())
        if choice == 1:
            self.show_schedule(db)
        elif choice == 2:
            self.send_pm(db)
        elif choice == 3:
            self.cancel_appointment(db)
        elif choice == 4:
            self.accept_appointment(db)
        elif choice == 5:
            self.add_visit_time(db)
