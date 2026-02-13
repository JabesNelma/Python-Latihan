# Nilai Maksimum dan Minimum
print("=== NILAI MAKSIMUM & MINIMUM ===")

try:
    input_str = input("Masukkan angka-angka pisahkan spasi: ")
    angka = list(map(int, input_str.split()))
    if angka:
        maks = max(angka)
        minim = min(angka)
        print(f"Angka: {angka}")
        print(f"Nilai maksimum: {maks}")
        print(f"Nilai minimum: {minim}")
    else:
        print("Tidak ada angka yang dimasukkan.")
except ValueError:
    print("Input harus angka dan dipisah spasi.")