from run import create_app

# Buat instance aplikasi Flask menggunakan fungsi factory
app = create_app()

# Tambahkan ini jika Anda menjalankan aplikasi secara langsung dengan Python
if __name__ == "__main__":
    app.run()
