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

    def show_prescription(self, db):
        sql = """
        SELECT prescription_id, description
        FROM prescription
        WHERE patient_id= %s
        """

        drugs_sql = """
        SELECT d.name
        FROM prescription_drug p
        INNER JOIN drug d
        ON d.drug_id = p.drug_id
        WHERE prescription_id = %s
        """

        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute(drugs_sql, (row[0],))
            drugs = cursor.fetchall()
            print("""
            Prescription id = {}
            Description = {}
            
            Drugs : {}
            """.format(row[0], row[1], drugs))

    def show_tests(self, db):
        sql = """
        SELECT diagnosis_id, description
        FROM diagnosis
        WHERE patient_id= %s
        """

        tests_sql = """
        SELECT d.name
        FROM diagnosis_test p
        INNER JOIN test d
        ON d.test_id = p.test_id
        WHERE diagnosis_id = %s
        """

        cursor = db.cursor()
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute(tests_sql, (row[0],))
            tests = cursor.fetchall()
            print("""
            Diagnosis id = {}
            Description = {}

            Tests : {}
            """.format(row[0], row[1], tests))

    def show_menu(self, db):
        print("1 - To see the timetable :")
        print("2 - Request a visit date (choose id of visit date from timetable) : ")
        print("3 - See prescription :")
        print("4 - See tests :")
        choice = int(input())
        if choice == 1:
            self.show_free_visit_times(db)
        elif choice == 2:
            self.request_visit_date(db)
        elif choice == 3:
            self.show_prescription(db)
        elif choice == 4:
            self.show_tests(db)

