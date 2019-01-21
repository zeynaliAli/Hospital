from model.user import User


class Accounting(User):

    @staticmethod
    def init_db(db):
        sql = """
        CREATE TABLE IF NOT EXISTS factor
        factor_id            int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        timetable_id         int NOT NULL,
        visit_price          varchar(50) UNIQUE,
        payed                int,
        FOREIGN KEY (timetable_id) REFERENCES timetable(timetable_id)
        """
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.close()
        db.commit()