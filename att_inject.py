import csv
import psycopg2

# Koneksi ke PostgreSQL
username = 'lecture2024'
password = 'Ojolali123'
host = 'lecture-dss-db.mekarsa.com'
port = '54321'
database = 'tourist'
table_name = 'tourist_attractions'

# Membuat koneksi psycopg2
conn = psycopg2.connect(
    host=host,
    port=port,
    user=username,
    password=password,
    database=database
)
cur = conn.cursor()

# Membaca file CSV dan melakukan insert dengan pengecekan
csv_file_path = 'tourist-destination.csv'
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)  # Membaca header, sesuaikan jika CSV Anda tidak memiliki header
    print(header)

    for row in csv_reader:
        print(row)

        check_query = f"""
        SELECT EXISTS(SELECT 1 FROM {table_name} WHERE name = %s)
        """

        cur.execute(check_query, (row[1],))  # Asumsikan id berada di kolom pertama (index 0)
        exists = cur.fetchone()[0]
        print(exists)

        # Jika data belum ada, lakukan INSERT
        if not exists:
            insert_query = f"""
            INSERT INTO {table_name} (name, entry_price, facility, stars, reviews, user_id, lat, lon, category_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (row[1], row[5], row[6], row[4], row[5], 2, row[2], row[3], row[0])  # Sesuaikan dengan urutan kolom di tabel Anda
            cur.execute(insert_query, values)

# Commit transaksi dan tutup koneksi
conn.commit()
cur.close()
conn.close()
print("Data berhasil diimpor dengan pengecekan manual.")
