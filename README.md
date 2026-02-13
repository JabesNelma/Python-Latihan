# 🐍 Kumpulan Latihan Python — Dasar hingga Menengah

Repositori ini berisi **25 program Python** yang mencakup berbagai konsep dasar hingga menengah. Dibuat oleh **Jabes** sebagai latihan dan referensi belajar Python.

---

## 📚 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Daftar Program](#-daftar-program)
- [Konsep yang Dipelajari](#-konsep-yang-dipelajari)
- [Cara Menjalankan](#-cara-menjalankan)
- [Struktur Folder](#-struktur-folder)
- [Lisensi](#-lisensi)

---

## 🎯 Tentang Proyek

Repositori ini adalah kumpulan program latihan Python yang dirancang untuk memperkuat pemahaman konsep-konsep fundamental pemrograman, mulai dari operasi string, struktur kontrol, fungsi, rekursi, generator, file I/O, hingga penggunaan modul standar Python.

---

## 📋 Daftar Program

### 🔤 String & Teks
| No | File | Deskripsi | Konsep Utama |
|----|------|-----------|--------------|
| 1 | `balik_string.py` | Membalikkan string yang diinput pengguna | String slicing `[::-1]` |
| 2 | `cek_palindrom.py` | Mengecek apakah sebuah kata/kalimat adalah palindrom | String manipulation, `.lower()`, `.replace()` |
| 3 | `frekuensi_huruf.py` | Menghitung frekuensi kemunculan setiap huruf dalam teks | Dictionary sebagai counter, `.get()`, `sorted()` |
| 4 | `hitung_kata.py` | Menghitung jumlah kata dalam sebuah kalimat | `.split()`, `len()` |

### 🔢 Angka & Matematika
| No | File | Deskripsi | Konsep Utama |
|----|------|-----------|--------------|
| 5 | `bilangan_ganjil_genap.py` | Mengecek bilangan ganjil atau genap | Operator modulo `%` |
| 6 | `cek_prima.py` | Mengecek apakah bilangan adalah bilangan prima | Algoritma prima dengan optimasi `√n` |
| 7 | `faktorial.py` | Menghitung faktorial bilangan non-negatif | **Rekursi** |
| 8 | `fibonacci.py` | Menghasilkan deret Fibonacci sejumlah n suku | Iteratif, tuple unpacking |
| 9 | `kpk_fpb.py` | Menghitung KPK dan FPB dua bilangan | `math.gcd()`, rumus $KPK = \frac{\|a \times b\|}{FPB}$ |
| 10 | `konversi_biner.py` | Konversi antara desimal dan biner | `bin()`, `int()` dengan parameter base |
| 11 | `konversi_suhu.py` | Konversi suhu antara Celsius dan Fahrenheit | Formula: $F = C \times \frac{9}{5} + 32$ |

### 📊 List & Dictionary
| No | File | Deskripsi | Konsep Utama |
|----|------|-----------|--------------|
| 12 | `jumlah_list.py` | Menjumlahkan semua elemen dalam list | `map()`, `sum()` |
| 13 | `nilai_max_min.py` | Mencari nilai maksimum dan minimum dalam list | `max()`, `min()` |
| 14 | `hapus_duplikat.py` | Menghapus elemen duplikat dengan mempertahankan urutan | Deduplikasi tanpa `set()` |
| 15 | `list_comprehension.py` | Membuat list kuadrat, genap, dan ganjil | **List comprehension** |
| 16 | `dict_comprehension.py` | Membuat dictionary pemetaan bilangan ke kuadratnya | **Dictionary comprehension** |
| 17 | `gabung_dict.py` | Menggabungkan dua dictionary | Dictionary unpacking `**` |

### 🧮 Kalkulator & Utilitas
| No | File | Deskripsi | Konsep Utama |
|----|------|-----------|--------------|
| 18 | `kalkulator.py` | Kalkulator sederhana (+, −, ×, ÷) | Loop `while True`, `break`/`continue` |
| 19 | `kalkulator_bmi.py` | Menghitung Body Mass Index (BMI) | Formula $BMI = \frac{berat}{tinggi^2}$, if/elif |
| 20 | `luas_bangun.py` | Menghitung luas persegi, lingkaran, segitiga | `math.pi`, formula geometri |

### ⚙️ Konsep Lanjutan
| No | File | Deskripsi | Konsep Utama |
|----|------|-----------|--------------|
| 21 | `error_handling.py` | Demonstrasi penanganan error lengkap | `try`/`except`/`else`/`finally` |
| 22 | `file_handler.py` | Membaca dan menulis file teks | File I/O, `with` statement, context manager |
| 23 | `generator_mundur.py` | Hitung mundur menggunakan generator Python | **Generator** (`yield`), lazy evaluation |
| 24 | `pola_bintang.py` | Mencetak pola segitiga siku-siku dan sama kaki | Nested loop, string repetition |
| 25 | `tebak_angka.py` | Permainan tebak angka 1–100 | `random` module, game loop |

---

## 🧠 Konsep yang Dipelajari

| Kategori | Konsep |
|----------|--------|
| **Dasar** | Variabel, tipe data, input/output, operator aritmatika & modulo |
| **Kontrol Alur** | `if`/`elif`/`else`, `for`, `while`, `break`/`continue` |
| **String** | Slicing, `.lower()`, `.replace()`, `.split()`, `.isalpha()` |
| **Fungsi** | Definisi fungsi, parameter, return value |
| **Rekursi** | Fungsi rekursif (faktorial) |
| **Struktur Data** | List, Dictionary, tuple unpacking |
| **Comprehension** | List comprehension, dictionary comprehension |
| **Generator** | `yield`, lazy evaluation |
| **Error Handling** | `try`/`except`/`else`/`finally`, `ValueError`, `ZeroDivisionError` |
| **File I/O** | `open()`, `with` statement, mode `w`/`r` |
| **Modul Standar** | `math`, `random` |
| **Formatting** | f-string, format specifier (`.2f`) |

---

## 🚀 Cara Menjalankan

### Prasyarat
- **Python 3.6+** terinstal di sistem Anda

### Menjalankan Program

```bash
# Clone repositori
git clone https://github.com/JabesNelma/Python-Latihan.git
cd Python-Latihan/lat2

# Jalankan program yang diinginkan
python3 nama_file.py
```

### Contoh

```bash
# Menjalankan kalkulator BMI
python3 kalkulator_bmi.py

# Menjalankan permainan tebak angka
python3 tebak_angka.py

# Menjalankan generator hitung mundur
python3 generator_mundur.py
```

---

## 📁 Struktur Folder

```
lat2/
├── balik_string.py          # Membalikkan string
├── bilangan_ganjil_genap.py # Cek ganjil/genap
├── cek_palindrom.py         # Cek palindrom
├── cek_prima.py             # Cek bilangan prima
├── dict_comprehension.py    # Dictionary comprehension
├── error_handling.py        # Error handling lengkap
├── faktorial.py             # Faktorial (rekursi)
├── fibonacci.py             # Deret Fibonacci
├── file_handler.py          # Baca/tulis file
├── frekuensi_huruf.py       # Frekuensi huruf
├── gabung_dict.py           # Gabung dictionary
├── generator_mundur.py      # Generator hitung mundur
├── hapus_duplikat.py        # Hapus duplikat list
├── hitung_kata.py           # Hitung kata
├── jumlah_list.py           # Jumlah elemen list
├── kalkulator.py            # Kalkulator sederhana
├── kalkulator_bmi.py        # Kalkulator BMI
├── konversi_biner.py        # Konversi desimal ↔ biner
├── konversi_suhu.py         # Konversi suhu
├── kpk_fpb.py               # KPK & FPB
├── list_comprehension.py    # List comprehension
├── luas_bangun.py           # Luas bangun datar
├── nilai_max_min.py         # Nilai max & min
├── pola_bintang.py          # Pola bintang
├── tebak_angka.py           # Permainan tebak angka
└── README.md                # Dokumentasi
```

---

## 📄 Lisensi

© 2021 Jabes. All rights reserved.