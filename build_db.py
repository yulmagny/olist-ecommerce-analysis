#!/usr/bin/env python3
"""
build_db.py — Membangun database SQLite (foo.db) dari berkas CSV Olist.

Dataset: Brazilian E-Commerce Public Dataset by Olist
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Cara pakai
----------
1. Unduh & ekstrak dataset Olist dari Kaggle (tautan di atas).
2. Letakkan SEMUA berkas .csv di dalam folder `data/`.
3. Jalankan:

       python build_db.py

   -> Menghasilkan `data/foo.db` dengan satu tabel per berkas CSV.

Catatan: nama tabel = nama berkas tanpa ekstensi
(mis. olist_orders_dataset.csv -> tabel `olist_orders_dataset`),
persis seperti yang dipakai di notebook analisis.
"""
import argparse
import sqlite3
import sys
from pathlib import Path

import pandas as pd

# 9 tabel inti yang dipakai notebook (untuk pengecekan kelengkapan)
EXPECTED = {
    "olist_customers_dataset",
    "olist_geolocation_dataset",
    "olist_order_items_dataset",
    "olist_order_payments_dataset",
    "olist_order_reviews_dataset",
    "olist_orders_dataset",
    "olist_products_dataset",
    "olist_sellers_dataset",
    "product_category_name_translation",
}


def build(data_dir: Path, db_path: Path) -> None:
    csv_files = sorted(data_dir.glob("*.csv"))
    if not csv_files:
        sys.exit(
            f"\u274c Tidak ada berkas .csv di '{data_dir}/'.\n"
            f"   Unduh dataset Olist dari Kaggle lalu taruh CSV-nya di folder itu:\n"
            f"   https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"
        )

    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()  # mulai dari database yang bersih

    conn = sqlite3.connect(db_path)
    created = set()
    try:
        for csv in csv_files:
            table = csv.stem
            # encoding='utf-8-sig' otomatis membuang karakter BOM
            # (mis. pada product_category_name_translation) agar nama kolom bersih.
            df = pd.read_csv(csv, encoding="utf-8-sig")
            df.to_sql(table, conn, if_exists="replace", index=False)
            created.add(table)
            print(f"  \u2713 {table:<38} {df.shape[0]:>8,} baris \u00d7 {df.shape[1]} kolom")
        conn.commit()
    finally:
        conn.close()

    print(f"\n\u2705 Selesai. Database tersimpan di: {db_path}")

    missing = EXPECTED - created
    extra = created - EXPECTED
    if missing:
        print("\n\u26a0\ufe0f  Tabel Olist yang diharapkan TIDAK ditemukan:")
        for t in sorted(missing):
            print(f"     - {t}")
        print("   Periksa lagi apakah semua CSV Olist sudah ada di folder data/.")
    if extra:
        print("\n\u2139\ufe0f  Tabel tambahan (di luar 9 tabel inti Olist) ikut dibuat:")
        for t in sorted(extra):
            print(f"     - {t}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Bangun foo.db dari berkas CSV Olist.")
    ap.add_argument("--data-dir", default="data",
                    help="Folder berisi berkas CSV (default: data)")
    ap.add_argument("--db", default=None,
                    help="Path output database (default: <data-dir>/foo.db)")
    args = ap.parse_args()

    data_dir = Path(args.data_dir)
    db_path = Path(args.db) if args.db else data_dir / "foo.db"

    print(f"\U0001f4e6 Membangun {db_path} dari CSV di '{data_dir}/' ...\n")
    build(data_dir, db_path)


if __name__ == "__main__":
    main()
