import sqlite3

conn = sqlite3.connect("database_fauna.db")
cursor = conn.cursor()

# Jalankan Query SELECT WHERE OR
cursor.execute("SELECT * FROM Fauna WHERE asal= 'Sumatera' OR jml_skrng > 500 ")
dataFauna = cursor.fetchall()

# Tampilkan dalam format tabel
if len(dataFauna) > 0:
    print("-" * 100)
    print(
        "{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            "ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"
        )
    )
    print("-" * 100)
    for value in dataFauna:
        print(
            "{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(
                value[0], value[1], value[2], value[3], value[4], value[5]
            )
        )
    else:
        print("*" * 100)
        print(
            "Data diatas, Berdasarkan Hewan yang Berasal dari Sumatera dan Jumlah Lebih dari 500"
        )

# Tutup Koneksi
conn.close()