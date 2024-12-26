from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Fungsi untuk mengatur game
@app.route("/", methods=["GET", "POST"])
def tebak_goa():
    cuypy = random.randint(1, 5)  # Posisi acak Cuypy
    hasil = ""
    pilihan_kamu = None
    nama_kamu = None
    yakin = None

    if request.method == "POST":
        # Mengambil data dari form
        nama_kamu = request.form.get("nama_kamu")
        pilihan_kamu = int(request.form.get("pilihan"))
        yakin = request.form.get("yakin")

        # Validasi pilihan jika yakin 'yes'
        if yakin == 'yes':
            if cuypy == pilihan_kamu:
                hasil = f"🎉 Selamat, {nama_kamu}! Kamu benar! Cuypy bersembunyi di goa nomor {cuypy}."
            else:
                hasil = f"😢 Maaf, {nama_kamu}. Tebakan kamu salah. Cuypy bersembunyi di goa nomor {cuypy}."
        else:
            hasil = "Silakan pilih ulang goa jika yakin sudah berubah."

    return render_template("index.html", hasil=hasil, cuypy=cuypy, pilihan_kamu=pilihan_kamu, nama_kamu=nama_kamu, yakin=yakin)

if __name__ == "__main__":
    app.run(debug=True)
