# Pola Bintang
print("=== POLA BINTANG ===")

try:
    tinggi = int(input("Masukkan tinggi segitiga: "))
    print("Segitiga siku-siku:")
    for i in range(1, tinggi + 1):
        print("*" * i)

    print("\nSegitiga sama kaki:")
    for i in range(1, tinggi + 1):
        print(" " * (tinggi - i) + "*" * (2*i - 1))
except ValueError:
    print("Input harus angka bulat.")