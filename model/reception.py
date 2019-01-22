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

        reception_sql = """
        CREATE TABLE IF NOT EXISTS reception (
        reception_id        int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        timetable_id        int NOT NULL,
        patient_id          int NOT NULL,
        FOREIGN KEY (timetable_id) REFERENCES timetable(timetable_id),
        FOREIGN KEY (patient_id) REFERENCES user(user_id)
        )
        """
        cursor = db.cursor()
        cursor.execute(timetable_sql)
        cursor.execute(reception_sql)
        cursor.close()
        db.commit()

    def cancel_visit_request(self, db):
        time_id = int(input("Enter id of visit time you want to cancel : \n"))
        sql = """
                UPDATE timetable
                SET patient_id = null
                WHERE timetable_id = %s
                """
        cursor = db.cursor()
        cursor.execute(sql, (time_id,))
        cursor.close()
        db.commit()
        print("Done!")
        self.show_menu(db)

    def send_visit_request(self, db):
        time_id = int(input("Enter id of visit time you want to set : \n"))
        patient_id = int(input("Enter id of patient you want to set time for : \n"))
        sql = """
        UPDATE timetable
        SET patient_id = %s
        WHERE timetable_id = %s
        """
        cursor = db.cursor()
        cursor.execute(sql, (patient_id, time_id))
        cursor.close()
        db.commit()
        print("Done!")
        self.show_menu(db)

    def show_visit_requests(self, db):
        sql = """
        SELECT 
            r.timetable_id,
            t.visit_date,
            d.username,
            d.mail,
            p.user_id,
            p.username,
            p.mail
        FROM reception r
        INNER JOIN timetable t
        ON r.timetable_id = t.timetable_id
        INNER JOIN user d
        ON d.user_id = t.doctor_id
        INNER JOIN user p
        ON p.user_id = r.patient_id
        """
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        db.commit()
        for row in rows:
            print("""
            ID = {}
            
            Time = {}
            
            For Doctor : 
                Doctor username = {}
                Doctor email = {}
            
            Requested by patient :
                Patient id = {}
                Patient username = {}
                Patient email = {}
            
            ______________________________
            
            """.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        self.show_menu(db)

    def show_menu(self, db):
        print("1 - For see requested times: ")
        print("2 - To send a requested time for Doctor:")
        print("3 - To cancel a request which is sent to doctor")
        choice = int(input())
        if choice == 1:
            self.show_visit_requests(db)
        elif choice == 2:
            self.send_visit_request(db)
        elif choice == 3:
            self.cancel_visit_request(db)


