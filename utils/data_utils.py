from random import randint

import MySQLdb
from faker import Faker

from model.user import User

db = MySQLdb.connect("localhost", "root", "suchadream", charset='utf8', use_unicode=True)
sql = "CREATE DATABASE IF NOT EXISTS hospital DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
sql_use = "USE hospital;"
cursor = db.cursor()
cursor.execute(sql)
cursor.execute(sql_use)
cursor.close()
db.commit()

# fake = Faker()
#
# u1 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-
# ..............................................................00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`db.com",  randint(1, 6))
# u2 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u3 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u4 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u5 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u6 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u7 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u9 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() +  "@fum-db.com",  randint(1, 6))
# u10 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u11 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u12 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u13 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u14 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u15 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u16 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
# u17 = User(fake.last_name(), fake.last_name(), fake.msisdn(), fake.first_name() + "@fum-db.com", randint(1, 6))
#
#
# u1.save(db)
# u2.save(db)
# u3.save(db)
# u4.save(db)
# u5.save(db)
# u6.save(db)
# u7.save(db)
# u9.save(db)
# u10.save(db)
# u11.save(db)
# u12.save(db)
# u13.save(db)
# u14.save(db)
# u15.save(db)
# u16.save(db)
# u17.save(db)








# sql = """
#         INSERT INTO timetable
#         (doctor_id, visit_date)
#         VALUES
#         (%s, %s)
#         """
# cursor = db.cursor()
# cursor.execute(sql, (8, '2010-06-13 13:55'))
# cursor.close()
# db.commit()

#
# sql = """
# UPDATE timetable
# SET patient_id = 7
# WHERE doctor_id = 8
# """
# cursor = db.cursor()
# cursor.execute(sql)
# cursor.close()
# db.commit()
