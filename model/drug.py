class Drug:
    def __init__(self,
                 name,
                 description,
                 price,
                 expire_time):
        self.name = name
        self.description = description
        self.price = price
        self.expire_time = expire_time

    def save(self, db):
        sql = """
        INSERT INTO drug
        (name, description, price, expire_date)
        VALUES
        (%s, %s, %s, %s)
        """
        cursor = db.cursor()
        cursor.execute(sql, (self.name, self.description, self.price, self.expire_time))
        cursor.close()
        db.commit()

