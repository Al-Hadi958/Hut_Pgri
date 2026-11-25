from flask import Flask, render_template

app = Flask(__name__)

GALERI_GURU = [
    {
        "file": "foto1.jpg",
        "judul": "Kebersamaan Busana Adat",
        "ket": "Potret penuh warna keluarga besar SMA Negeri 1 Kabangka dalam balutan busana adat."
    },
    {
        "file": "foto2.jpg",
        "judul": "Semangat & Senyum Hangat",
        "ket": "Momen akrab para pendidik dengan nuansa merah muda yang penuh keakraban."
    },
    {
        "file": "foto3.jpg",
        "judul": "Pengabdian di Depan Ruang Kelas",
        "ket": "Sosok-sosok teladan yang setia membimbing langkah demi langkah siswa."
    },
    {
        "file": "foto4.jpg",
        "judul": "Dedikasi & Literasi Digital",
        "ket": "Guru-guru SMA Negeri 1 Kabangka bersama perangkat kerja di lingkungan sekolah."
    },
    {
        "file": "foto5.jpg",
        "judul": "Keluarga Besar Aksara 23–26",
        "ket": "Kebersamaan guru dan siswa di lapangan SMA Negeri 1 Kabangka."
    },
    {
        "file": "foto6.jpg",
        "judul": "Silaturahmi Penuh Makna",
        "ket": "Potret kebersamaan dalam balutan seragam batik nuansa biru."
    },
    {
        "file": "foto7.jpg",
        "judul": "Solidaritas Pendidik",
        "ket": "Kekompakan dan semangat pengabdian dewan guru di halaman sekolah."
    },
    {
        "file": "foto8.jpg",
        "judul": "Gerbang SMA Negeri 1 Kabangka",
        "ket": "Kebersamaan penuh keanggunan di depan papan nama SMA Negeri 1 Kabangka."
    },
    {
        "file": "foto9.jpg",
        "judul": "Jejak Langkah & Apresiasi",
        "ket": "Momen hangat bersama siswa dan karangan bunga tanda hormat untuk guru."
    },
]


@app.route("/")
def index():
    return render_template("index.html", galeri=GALERI_GURU)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)