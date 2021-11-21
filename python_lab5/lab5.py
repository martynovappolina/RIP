import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c = db.cursor()
c.execute("INSERT INTO films (name, description) VALUES (%s, %s);", ('Тернер и Хуч', 'Полицейский Скотт Тернер (Том Хэнкс) отрабатывает последние три дня в тихом городке в Калифорнии. После этого его направляют с повышением на работу в Сакраменто. Тернеру поручают расследовать убийство его друга Амоса Рида (Джон МакИнтайр), единственным свидетелем которого был его пес Хуч.'))
db.commit()
c.close()
db.close()