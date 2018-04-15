import MySQLdb

"Пример запроса к БД"
conn = MySQLdb.connect('host', 'user', 'password', 'db')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
