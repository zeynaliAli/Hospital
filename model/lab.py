from model.test import Test
from model.user import User


class Lab(User):

    @staticmethod
    def init_db(db):

        diagnosis_sql = """
        CREATE TABLE IF NOT EXISTS diagnosis
        (prescription_id   int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        doctor_id          int NOT NULL,
        patient_id         int NOT NULL,
        description        text,
        FOREIGN KEY (doctor_id)  REFERENCES user(user_id),
        FOREIGN KEY (patient_id) REFERENCES user(user_id))
        """

        test_sql = """
        CREATE TABLE IF NOT EXISTS test (
        test_id         int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        name            varchar(50),
        price           int,
        description     text
        )
        """

        diagnosis_test_sql = """
        CREATE TABLE IF NOT EXISTS  diagnosis_drug (
        d_t_id              int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        diagnosis_id        int NOT NULL,
        test_id             int NOT NULL
        )
        """

        cursor = db.cursor()
        cursor.execute(diagnosis_sql)
        cursor.execute(test_sql)
        cursor.execute(diagnosis_test_sql)
        cursor.close()
        db.commit()

    def save_test(self, db):
        name = input("Enter test name : \n")
        description = input("Enter test description : \n")
        price = int(input("Enter test price : \n"))

        test = Test(name, description, price)
        test.save(db)
        print("Done!")
        self.show_menu(db)

    def give_tests(self, db):
        diagnosis_id = int(input("Enter patient diagnosis id : \n"))
        diagnosis_tests_sql = """
        SELECT test_id
        FROM diagnosis_test
        WHERE diagnosis_id = %s
        """
        cursor = db.cursor()
        cursor.execute(diagnosis_tests_sql, (diagnosis_id,))
        rows = cursor.fetchall()
        test_sql = """
        SELECT name, description, price
        FROM test
        WHERE test_id = %s
        """
        for row in rows:
            cursor.execute(test_sql, (row[0],))
            test = cursor.fetcone()
            print(test)
        print("Done!")
        self.show_menu(db)

    def show_menu(self, db):
        print("1 - Save a test")
        print("2 - Give tests")
        choice = int(input())
        if choice == 1:
            self.save_test(db)
        elif choice == 2:
            self.give_tests(db)
