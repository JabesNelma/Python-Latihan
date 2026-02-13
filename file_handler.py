# Membaca dan Menulis File
print("=== FILE HANDLER ===")

print("1. Tulis ke file")
print("2. Baca file")
pilihan = input("Pilih menu (1/2): ")

if pilihan == '1':
    nama_file = input("Nama file (contoh: data.txt): ")
    teks = input("Masukkan teks yang ingin ditulis:\n")
    with open(nama_file, 'w') as f:
        f.write(teks + "\n")
    print(f"Teks telah ditulis ke {nama_file}.")
elif pilihan == '2':
    nama_file = input("Nama file yang akan dibaca: ")
    try:
        with open(nama_file, 'r') as f:
            isi = f.read()
        print("Isi file:")
        print(isi)
    except FileNotFoundError:
        print("File tidak ditemukan.")
else:
    print("Pilihan tidak valid.")