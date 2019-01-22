class Test:
    def __init__(self,
                 name,
                 description,
                 price):
        self.name = name
        self.description = description
        self.price = price

    def save(self, db):
        sql = """
        INSERT INTO test
        (name, description, price)
        VALUES
        (%s, %s, %s)
        """
        cursor = db.cursor()
        cursor.execute(sql, (self.name, self.description, self.price))
        cursor.close()
        db.commit()

