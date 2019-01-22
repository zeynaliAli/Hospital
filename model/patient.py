from model.user import User


class Patient(User):

    @staticmethod
    def init_db(db):
        return

    def request_visit_date(self, db):
        time_request_id = int(input("Enter id of visit time : \n"))
        sql = """
        INSERT INTO reception
        (timetable_id, patient_id)
        VALUES
        (%s, %s)
        """
        cursor = db.cursor()
        cursor.execute(sql, (time_request_id, self.id))
        db.commit()
        print("Done!")
        self.show_menu(db)

    def show_free_visit_times(self, db):
        sql = """
        SELECT t.timetable_id, t.visit_date, u.username, u.mail
        FROM timetable t
        INNER JOIN user u ON u.user_id = t.doctor_id
        WHERE t.patient_id is NULL
        """
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print("""
            Free Visit Time :
            
            id = {}
            time = {}
            
            Doctor :
            
            username = {}
            email = {}
            _____________________________________
            
            """.format(row[0], row[1], row[2], row[3]))
        cursor.close()
        db.commit()
        self.show_menu(db)

    def show_menu(self, db):
        print("1 - to see the timetable :")
        print("2 - request a visit date (choose id of visit date from timetable) : ")
        choice = int(input())
        if choice == 1:
            self.show_free_visit_times(db)
        elif choice == 2:
            self.request_visit_date(db)

