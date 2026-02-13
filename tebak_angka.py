# Tebak Angka
import random

print("=== TEBAK ANGKA ===")
print("Saya memikirkan angka antara 1 sampai 100.")
angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    try:
        tebak = int(input("Tebakan Anda: "))
        percobaan += 1
        if tebak < angka_rahasia:
            print("Terlalu kecil.")
        elif tebak > angka_rahasia:
            print("Terlalu besar.")
        else:
            print(f"Selamat! Anda menebak dalam {percobaan} kali.")
            break
    except ValueError:
        print("Input harus angka bulat.")