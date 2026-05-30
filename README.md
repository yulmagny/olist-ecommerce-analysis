# Analisis Penjualan E-Commerce Olist — End-to-End (SQL → Python → Insight Bisnis)

**Ringkasan singkat**
Proyek analisis data menyeluruh terhadap ~119.000 transaksi marketplace Olist (Brasil, 2016–2018) — mulai dari ekstraksi data mentah dengan SQL, penggabungan 9 tabel, pembersihan, hingga analisis dan presentasi bisnis berisi rekomendasi yang dapat langsung ditindaklanjuti.

**Peran:** Data Analyst
**Tools:** SQL (SQLite) · Python (pandas) · Matplotlib · Seaborn

---

## Skill yang Ditunjukkan
Ekstraksi data dengan SQL · penggabungan multi-tabel (relational joins) · pembersihan & penanganan nilai kosong · feature engineering · analisis eksploratif (EDA) · visualisasi data · penerjemahan temuan menjadi rekomendasi bisnis.

## Pertanyaan Bisnis
1. Bagaimana tren penjualan dari waktu ke waktu?
2. Di mana penjualan paling terkonsentrasi secara geografis?
3. Seberapa tinggi loyalitas dan keterlibatan pelanggan?
4. Kategori produk, metode pembayaran, dan waktu mana yang paling berpengaruh?

## Proses Singkat
Menarik 9 tabel dari database SQLite → menggabungkannya lewat kunci relasional menjadi satu dataset (~119.000 baris, 40+ kolom) → membersihkan (nilai kosong per kolom, konversi tanggal, hapus duplikat) → menambah kolom turunan (waktu pembelian, total nilai pesanan) → menganalisis & memvisualisasikan.

## Temuan Utama
- **Penjualan tumbuh kuat dari tahun ke tahun.** 2018 yang belum genap setahun (data berakhir Oktober) sudah melampaui total penuh 2017 — indikasi pertumbuhan nyata, bukan sekadar efek rentang waktu.
- **Sangat terkonsentrasi secara geografis.** São Paulo (15.540 pelanggan unik) dan Rio de Janeiro (6.882) mendominasi; kontribusi kota lain jauh lebih kecil.
- **Retensi & keterlibatan rendah.** Mayoritas pelanggan hanya membeli satu kali, dan sebagian besar transaksi tidak menghasilkan ulasan.
- **Terpusat pada sedikit kategori & condong ke awal pekan.** Lima kategori teratas (bed_bath_table, health_beauty, sports_leisure, furniture_decor, computers_accessories) mendominasi; pesanan memuncak Senin–Selasa dan terendah di akhir pekan. Pembayaran didominasi kartu kredit.

## Rekomendasi Bisnis
1. **Retensi pelanggan** — program loyalitas / kupon follow-up untuk mengubah pembeli sekali-jalan menjadi pelanggan berulang (leverage pertumbuhan terbesar).
2. **Ekspansi geografis** — kampanye pemasaran tersasar di kota tier-2 untuk mengurangi ketergantungan pada São Paulo & Rio.
3. **Diversifikasi pembayaran** — insentif (mis. diskon kecil) untuk mendorong metode pembayaran selain kartu kredit.
4. **Stabilisasi penjualan** — sesuaikan stok dan jadwalkan promosi pada hari/periode dengan penjualan sepi.

## Deliverable (bukti)
- **Notebook analisis (Python + SQL)** — proses lengkap dari ekstraksi hingga visualisasi. → [tautan ke GitHub/Drive]
- **Presentasi bisnis (27 slide)** — temuan & rekomendasi untuk pemangku kepentingan. → [tautan ke Drive/SlideShare]

---
*Dataset: Olist Brazilian E-Commerce (publik). Analisis & visualisasi dikerjakan dengan Python.*
# olist-ecommerce-analysis
