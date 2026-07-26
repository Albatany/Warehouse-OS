# WareHouse OS (Sistem Manajemen Gudang)

**Project UAS Mata Kuliah Algoritma Pemrograman**
Nama: Muhammad Aziz Syah Dani
NIM: F1E325063
Nilai akhir: **A**

## Tentang Project

WareHouse OS adalah simulasi sistem manajemen gudang yang dibangun untuk memenuhi tugas UAS mata kuliah Algoritma Pemrograman. Project ini terdiri dari beberapa modul Python yang masing-masing mendemonstrasikan konsep algoritma dan struktur data yang berbeda mulai dari logika dasar, algoritma sorting, algoritma searching, hingga struktur data Hash Table dengan studi kasus proses penerimaan, pengurutan, pencarian, dan pemetaan lokasi barang di gudang.

Setiap modul diuji dengan dataset sebanyak **100.000 (100rb) baris data barang** untuk melihat perbedaan performa nyata antar algoritma, tidak hanya berdasarkan teori kompleksitas Big-O saja.

## Daftar Modul

### Modul A: Alur Penerimaan Barang (Logika Dasar)
Mensimulasikan proses barang masuk ke gudang: cek fisik → input data → generate ID resi unik → simpan ke struktur data. Berfokus pada logika dasar pemrograman prosedural (flowchart, pseudocode, implementasi).
File: `modul_a.py`

### Modul B: Analisis Efisiensi Algoritma
Membandingkan Bubble Sort dan Quick Sort secara teori (kompleksitas waktu & ruang, best/worst/average case) sekaligus mengukur runtime aktual keduanya menggunakan modul `time` pada data barang.

### Modul C: Pengurutan Inventaris (Sorting)
Mengimplementasikan tiga algoritma sorting untuk kebutuhan berbeda:
- **Bubble Sort** → urutkan barang berdasarkan harga termurah (contoh algoritma sederhana, kurang efisien)
- **Selection Sort** → urutkan barang berdasarkan tahun kedaluwarsa (dipilih karena meminimalkan jumlah swap)
- **Quick Sort (rekursif)** → urutkan barang berdasarkan ID resi (mendemonstrasikan divide and conquer)

File: `modul_c.py` → menghasilkan output `data_barang_c.csv`

### Modul D: Pencarian Barang (Searching)
- **Linear Search** → cari barang berdasarkan nama (karena data tidak selalu terurut)
- **Binary Search** → cari barang berdasarkan ID resi (mensyaratkan data sudah diurutkan lebih dulu memakai Quick Sort dari Modul C)

File: `modul_d.py`

### Modul E: Penyimpanan Cepat (Hash Table)
Membangun struktur `HashTableLokasiRak` dengan teknik *separate chaining* untuk memetakan Kode Barang → Nomor Rak, sehingga lookup lokasi rak mendekati kompleksitas O(1) dibanding harus looping seluruh data.

File: `modul_e.py` → menghasilkan output `data_peta.csv`

## Struktur File

| File | Keterangan |
|---|---|
| `data_barang.py` | Struktur data `Barang` dan fungsi pembacaan data awal |
| `modul_a.py` | Implementasi Modul A (penerimaan barang) |
| `modul_c.py` | Implementasi Modul C (Bubble Sort, Selection Sort, Quick Sort) |
| `modul_d.py` | Implementasi Modul D (Linear Search, Binary Search) |
| `modul_e.py` | Implementasi Modul E (Hash Table) |
| `data_barang.csv` | Dataset awal barang gudang |
| `data_barang_c.csv` | Output hasil sorting dari `modul_c.py` — **diminta dosen untuk diexport khusus saat presentasi** |
| `data_peta.csv` | Output hasil pemetaan Kode Barang → Nomor Rak dari `modul_e.py` |

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan modul yang ingin diuji dari terminal:

```bash
python modul_a.py   # Simulasi penerimaan barang
python modul_c.py   # Sorting (Bubble, Selection, Quick) -> menghasilkan data_barang_c.csv
python modul_d.py   # Searching (Linear & Binary)
python modul_e.py   # Hash Table -> menghasilkan data_peta.csv
```

`modul_d.py` bergantung pada hasil sorting Quick Sort dari `modul_c.py`, dan `modul_e.py` membaca data barang untuk membangun hash table lokasi rak.

## Hasil Benchmark Sorting (100.000 data)

Dari seluruh algoritma sorting yang diuji, **Bubble Sort adalah yang paling lambat**, karena kompleksitas algoritmanya yang lebih rumit (perbandingan berpasangan berulang, kompleksitas rata-rata/terburuk O(n²)) dibanding Selection Sort maupun Quick Sort.

| Spesifikasi perangkat | Estimasi waktu Bubble Sort untuk 100rb data |
|---|---|
| Spek rendah | > 1 jam |
| Spek tinggi | ~5 menit |
| Spek sangat tinggi ("ultimate") | bisa tetap > 5 menit tergantung kondisi sistem saat itu |

Perbedaan waktu ini menunjukkan secara nyata mengapa pemilihan algoritma sorting yang tepat (misalnya Quick Sort untuk data besar) jauh lebih penting dibanding hanya mengandalkan algoritma yang paling mudah dipahami seperti Bubble Sort.

## Rencana Pengembangan

Untuk mempercepat proses sorting pada dataset besar, salah satu opsi pengembangan ke depan adalah menulis ulang bagian-bagian intensif komputasi (terutama Bubble Sort) ke bahasa **C atau C++**, karena kedua bahasa tersebut tergolong jauh lebih cepat dibanding Python untuk operasi komputasi berat semacam ini.

## Catatan Presentasi

Sesuai permintaan dosen saat presentasi, hanya hasil dari **Modul C** (`modul_c.py`) yang diexport ke CSV (`data_barang_c.csv`), karena file ini juga dipakai sebagai input data terurut untuk Binary Search di Modul D.
