# Hapus Duplikat dalam List
print("=== HAPUS DUPLIKAT ===")

try:
    input_str = input("Masukkan angka-angka pisahkan spasi: ")
    angka = list(map(int, input_str.split()))
    unik = []
    for item in angka:
        if item not in unik:
            unik.append(item)
    print(f"List asli: {angka}")
    print(f"Tanpa duplikat: {unik}")
except ValueError:
    print("Input harus angka dan dipisah spasi.")