import sqlite3
conn = sqlite3.connect("database/ratings.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS urls (url TEXT PRIMARY KEY, is_safe INTEGER)")
conn.commit()
conn.close()
print("資料庫建立完成")
