from model.user import User


class Pharmacy(User):

    @staticmethod
    def init_db(db):

        drug_sql = """
        CREATE TABLE IF NOT EXISTS drug
        drug_id          int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        name             varchar(150),
        desc             text,
        price            int,
        expire_date      datetime
        """

        prescription_drug_sql = """
        CREATE TABLE IF NOT EXIST  prescription_drug
        p_d_id           int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        prescription_id  int NOT NULL,
        drug_id          int NOT NULL
        """

        cursor = db.cursor()
        cursor.execute(drug_sql)
        cursor.execute(prescription_drug_sql)
        cursor.close()
        db.commit()