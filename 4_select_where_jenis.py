import sqlite3
koneksi = sqlite3.connect("database_fauna.db")

kursor = koneksi.cursor()
#mengambil swmua data dalam tabel dan tampilkan
kursor.execute("SELECT * FROM FAUNA WHERE jenis = 'Mamalia'")
# Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()
# membuat format table dengan method format
print("DATA FAUNA")
print("="*90)
print("{:<5} {:18} {:10} {:15} {:15} {:>20}".format("ID","Nama_Fauna","Jenis","Asal","Jumlah Saat Ini","Tahun Terakhir"))
print("-"*90)
# tampilkan data sesuai format tabel dg perulangan
for baris in baris_tabel :
    print("{:<5} {:18} {:10} {:16} {:15} {:>20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

koneksi.close()