# Pertemuan 05 Perulangan Python

Nama: Zahra Amelia  
NIM: 2225250044  
Kelas: S1 Pendidikan Matematika

## Tujuan

Menggunakan perulangan `for` dan `while` untuk menyelesaikan masalah iteratif.

## Cara Menjalankan

Jalankan program melalui terminal dengan perintah:

```bash
python latihan/01_tabel_perkalian.py
python latihan/02_jumlah_bilangan.py
python latihan/03_validasi_input.py
python latihan/04_hitung_genap.py
python kuis/kuis2_deret_aritmetika.py
```
## Algoritma Kuis 2

1. Masukkan suku pertama (a) dan beda (d).
2. Masukkan banyak suku (n).
3. Jika n kurang dari atau sama dengan 0, minta pengguna memasukkan n kembali sampai nilainya positif.
4. Atur nilai total menjadi 0.
5. Ulangi proses sebanyak n kali.
6. Hitung nilai suku dengan rumus a + i × d.
7. Tambahkan nilai suku ke dalam total dan tampilkan suku tersebut.
8. Setelah perulangan selesai, tampilkan jumlah seluruh suku.

## Hasil Pengujian

| Input (a, d, n) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| 2, 3, 5 | Suku: 2, 5, 8, 11, 14; Jumlah = 40.00 | Suku: 2.0, 5.0, 8.0, 11.0, 14.0; Jumlah = 40.00 | Berhasil |
| 10, -2, 4 | Suku: 10, 8, 6, 4; Jumlah = 28.00 | Suku: 10.0, 8.0, 6.0, 4.0; Jumlah = 28.00 | Berhasil |
| 1.5, 0.5, 3 | Suku: 1.5, 2.0, 2.5; Jumlah = 6.00 | Suku: 1.5, 2.0, 2.5; Jumlah = 6.00 | Berhasil |

## Refleksi

Kesalahan yang perlu diperhatikan dalam perulangan adalah mengatur nilai `total = 0` di dalam loop. Jika dilakukan, nilai total akan kembali menjadi 0 pada setiap iterasi sehingga hasil penjumlahan tidak terkumpul dengan benar. Perbaikannya adalah menginisialisasi `total = 0` sebelum perulangan dimulai, kemudian menambahkan setiap suku ke dalam total selama perulangan.