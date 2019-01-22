from datetime import datetime

from model.drug import Drug
from model.user import User


class Pharmacy(User):

    @staticmethod
    def init_db(db):

        drug_sql = """
        CREATE TABLE IF NOT EXISTS drug
        (drug_id         int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        name             varchar(150),
        description      text,
        price            int,
        expire_date      datetime)
        """

        prescription_drug_sql = """
        CREATE TABLE IF NOT EXISTS  prescription_drug
        (p_d_id           int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        prescription_id  int NOT NULL,
        drug_id          int NOT NULL)
        """

        cursor = db.cursor()
        cursor.execute(drug_sql)
        cursor.execute(prescription_drug_sql)
        cursor.close()
        db.commit()

    def save_drug(self, db):
        name = input("Enter drug name : \n")
        description = input("Enter drug description : \n")
        price = int(input("Enter drug price : \n"))
        exp_date = input("Enter drug expiration date (example : 2019-06-13 13:10)  \n")

        drug = Drug(name, description, price, exp_date)
        drug.save(db)
        print("Done!")
        self.show_menu(db)

    def give_drugs(self, db):
        prescription_id = int(input("Enter patient prescription id : \n"))
        prescription_drugs_sql = """
        SELECT drug_id
        FROM prescription_drug
        WHERE prescription_id = %s
        """
        cursor = db.cursor()
        cursor.execute(prescription_drugs_sql, (prescription_id,))
        rows = cursor.fetchall()
        drug_sql = """
        SELECT name, description, price, expire_date
        FROM drug
        WHERE drug_id = %s
        """
        for row in rows:
            cursor.execute(drug_sql, (row[0],))
            drug = cursor.fetcone()
            print(drug)
        print("Done!")
        self.show_menu(db)

    def filter_drugs_exp_date(self, db):

        expired_drugs_sql = """
        SELECT name, price, description
        FROM drug
        WHERE expire_date < %s
        """
        valid_drugs_sql = """
        SELECT name, price, description
        FROM drug
        WHERE expire_date > %s
        """

        print("Expired Drugs Are :")
        cursor = db.cursor()
        cursor.execute(expired_drugs_sql, (datetime.now(),))
        rows = cursor.fetchall()
        for row in rows:
            print("Name : {} - Price : {}\nDescription : {}".format(row[0], row[1], row[2]))

        print("Valid Drugs Are :")
        cursor = db.cursor()
        cursor.execute(valid_drugs_sql, (datetime.now(),))
        rows = cursor.fetchall()
        for row in rows:
            print("Name : {} - Price : {}\nDescription : {}".format(row[0], row[1], row[2]))

        print("_____________________________")
        self.show_menu(db)

    def show_menu(self, db):
        print("1 - Save a drug")
        print("2 - Get the prescription number (id) then Give the drugs")
        print("3 - filter drugs by expiration date")
        choice = int(input())
        if choice == 1:
            self.save_drug(db)
        if choice == 2:
            self.give_drugs(db)
        if choice == 3:
            self.filter_drugs_exp_date(db)
