# 📊 Analisis Penjualan E-Commerce Olist — End-to-End (SQL → Python → Insight Bisnis)

> Analisis data **end-to-end** marketplace terbesar di Brasil — dari ekstraksi data dengan SQL, pembersihan, hingga rekomendasi bisnis yang dapat ditindaklanjuti.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

---

## 📌 Ringkasan

Olist adalah marketplace terbesar di Brasil yang menghubungkan UMKM dengan pelanggan di seluruh negeri. Dataset publik ini berisi **±100.000 pesanan (2016–2018)** mencakup data pesanan, pelanggan, produk, pembayaran, ulasan, dan geolokasi — data komersial nyata yang telah dianonimkan.

Proyek ini menganalisis **perilaku pelanggan dan kinerja penjualan** secara menyeluruh, lalu menerjemahkan temuan menjadi rekomendasi bisnis.

## ❓ Pertanyaan Bisnis

1. Bagaimana karakteristik & demografi pelanggan, dan kota mana yang paling potensial?
2. Bagaimana pola perilaku pemesanan (frekuensi, waktu, metode pembayaran, kategori favorit)?
3. Seberapa puas pelanggan berdasarkan ulasan, dan bagaimana kaitannya dengan transaksi?
4. Bagaimana tren penjualan dari waktu ke waktu — naik, turun, atau musiman?
5. Rekomendasi bisnis apa yang bisa diambil dari temuan ini?

## 🔑 Temuan Utama

- **Mayoritas pelanggan hanya membeli satu kali** — banyak yang tanggal pembelian pertama & terakhirnya sama, indikasi kuat **retensi rendah**.
- **Aktivitas terpusat di kota besar** (São Paulo, Rio de Janeiro, Belo Horizonte) dengan jumlah pelanggan unik tertinggi.
- **Perbedaan aktivitas antar kota cukup signifikan**, membuka peluang strategi pemasaran berbeda per wilayah.
- Pelanggan dapat **disegmentasi berdasarkan frekuensi pesanan** untuk strategi retensi yang lebih tepat sasaran.
- Analisis memakai `customer_unique_id` (bukan `customer_id`) agar pelanggan dengan pembelian berulang teridentifikasi dengan benar.

## 💡 Rekomendasi Bisnis

1. **Retensi pelanggan** — kembangkan program loyalitas/insentif dan penawaran khusus bagi pembeli sekali-jalan agar kembali bertransaksi.
2. **Pemasaran tertarget** — pendekatan berbeda untuk kota beraktivitas rendah; manfaatkan hasil segmentasi pelanggan.
3. **Analisis lanjutan** — telusuri penyebab pembelian sekali-jalan dan gunakan **analisis kohort** untuk menangkap tren yang tak terlihat pada analisis snapshot.

## 🛠️ Tools & Teknologi

`Python` · `SQL (SQLite)` · `pandas` · `NumPy` · `SciPy` · `Matplotlib` · `Seaborn` · `Jupyter Notebook`

## 🔎 Alur Analisis

Notebook ini mengikuti siklus kerja data analyst yang lengkap:

| Tahap | Isi |
|------:|-----|
| 1 | **Pengambilan Data** — ekstraksi dari database dengan SQL |
| 2 | **Integrasi Data** — menggabungkan 9 tabel (join) |
| 3 | **Pembersihan Data** — menangani nilai hilang (null) |
| 4 | **Feature Engineering** — membuat kolom turunan (tanggal, total, kategori) |
| 5 | **Analisis Eksploratif (EDA)** — tren penjualan, produk & kategori |
| 6 | **Demografi Pelanggan** — pelanggan unik per kota, frekuensi |
| 7 | **Perilaku Pemesanan** — waktu, pembayaran, kategori favorit |
| 8 | **Ulasan & Kepuasan** — skor ulasan, tingkat kepuasan |
| 9 | **Deret Waktu** — tren penjualan & pola musiman |
| 10 | **Ringkasan Visual & Rekomendasi Bisnis** |

## 📊 Contoh Visualisasi

<!-- Ekspor 2–3 grafik andalanmu sebagai PNG ke folder images/, lalu hidupkan baris di bawah (hapus tanda komentar). -->
<!-- ![Tren Penjualan](images/tren_penjualan.png) -->
<!-- ![Segmentasi Pelanggan per Kota](images/segmentasi_pelanggan.png) -->

> 💡 Tip: README dengan beberapa grafik "andalan" jauh lebih menarik bagi recruiter. Cukup screenshot 2–3 grafik kunci dari notebook, simpan di folder `images/`, lalu aktifkan baris gambar di atas.

## 📂 Dataset

**Brazilian E-Commerce Public Dataset by Olist** — tersedia di Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Data dimuat dari database SQLite `data/foo.db`, yang dibangun dari berkas CSV Olist menggunakan `build_db.py`.

## ▶️ Cara Menjalankan

```bash
# 1. Clone repo
git clone https://github.com/yulmagny/olist-ecommerce-analysis.git
cd olist-ecommerce-analysis

# 2. (Opsional) pasang dependensi
pip install -r requirements.txt
```

3. Unduh dataset Olist dari Kaggle (tautan di atas), ekstrak, dan letakkan **semua berkas `.csv`** di folder `data/`.

```bash
# 4. Bangun database dari CSV
python build_db.py

# 5. Buka notebook lalu jalankan semua sel
jupyter notebook Analisis_Pelanggan_Ecommerce_Olist.ipynb
```

## 🗂️ Struktur Repository

```
olist-ecommerce-analysis/
├── Analisis_Pelanggan_Ecommerce_Olist.ipynb   # notebook analisis utama
├── build_db.py                                 # membangun data/foo.db dari CSV Olist
├── requirements.txt                            # daftar dependensi
├── README.md
├── images/                                     # screenshot grafik untuk README
└── data/                                        # CSV Olist + foo.db  (masuk .gitignore)
```

> Folder `data/` **tidak di-commit** (ada di `.gitignore`) karena berisi berkas besar. Siapa pun bisa membangunnya ulang lewat `build_db.py`.

## 👤 Tentang

**Yuli** — Forester yang beralih ke Data Analyst, dengan minat khusus di persimpangan **data lingkungan & analitik**.

🔗 LinkedIn: `https://linkedin.com/in/PROFIL-KAMU`  *(ganti dengan tautan profilmu)*

---

*Proyek portofolio untuk pembelajaran analisis data. Dataset © Olist, dipublikasikan di Kaggle.*
