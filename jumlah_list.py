# Jumlah Elemen List
print("=== JUMLAH ELEMEN LIST ===")

try:
    input_str = input("Masukkan angka-angka pisahkan spasi: ")
    angka = list(map(int, input_str.split()))
    total = sum(angka)
    print(f"Angka yang dimasukkan: {angka}")
    print(f"Jumlah: {total}")
except ValueError:
    print("Input harus angka dan dipisah spasi.")