from model.user import User


class Accounting(User):

    @staticmethod
    def init_db(db):
        sql = """
        CREATE TABLE IF NOT EXISTS factor (
        factor_id             int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        patient_id            int NOT NULL,
        price                 int,
        payed                 int,
        description           text,
        FOREIGN KEY (patient_id) REFERENCES user(user_id)
        )
        """
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.close()
        db.commit()

    def calculate_user_drug_debt(self, db, user_id):

        drugs_debt_sql = """
        SELECT SUM(d.price)
        FROM drug d
        INNER JOIN prescription_drug p_d
        ON p_d.drug_id = d.drug_id
        INNER JOIN prescription p
        ON p.prescription_id = p_d.prescription_id
        WHERE p.patient_id = %s
        """
        cursor = db.cursor()
        cursor.execute(drugs_debt_sql, (user_id,))
        price = int(cursor.fetchone())
        cursor.close()
        return price

    def calculate_user_test_debt(self, db, user_id):
        tests_debt_sql = """
        SELECT SUM(t.price)
        FROM test t
        INNER JOIN diagnosis_test d_t
        ON d_t.test_id = d.test_id
        INNER JOIN diagnosis d
        ON d.diagnosis_id = d_t.diagnosis_id
        WHERE d.patient_id = %s
        """
        cursor = db.cursor()
        cursor.execute(tests_debt_sql, (user_id,))
        price = int(cursor.fetchone())
        cursor.close()
        return price


    def calculate_user_debt(self, db):
        patient_id = input("What is Patient ID ?")
        tests_debt = self.calculate_user_test_debt(db, patient_id)
        drugs_debt = self.calculate_user_drug_debt(db, patient_id)
        print(tests_debt + drugs_debt)

    def show_menu(self, db):
        print(" 1 - How much should patient pay?")
        choice = int(input())
        if choice == 1:
            self.calculate_user_debt(db)