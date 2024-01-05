import sqlite3
koneksi = sqlite3.connect("database_fauna.db")
kursor = koneksi.cursor()

kursor.execute("SELECT SUM (jml_skrng) FROM FAUNA")
total = kursor.fetchone()[0]

print(f"Total Populasi :{total}")

koneksi.close()