import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c=db.cursor()
c.execute("INSERT INTO theatre (name, discription) VALUES (%s, %s);", ('Theater', 'Description'))
db.commit()
c.close()
db.close()