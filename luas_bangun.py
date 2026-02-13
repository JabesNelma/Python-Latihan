# Luas Bangun Datar
import math

print("=== LUAS BANGUN DATAR ===")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

try:
    pilihan = int(input("Pilih bangun (1/2/3): "))
    if pilihan == 1:
        s = float(input("Masukkan sisi: "))
        luas = s * s
        print(f"Luas persegi (sisi={s}) = {luas}")
    elif pilihan == 2:
        r = float(input("Masukkan jari-jari: "))
        luas = math.pi * r * r
        print(f"Luas lingkaran (r={r}) = {luas:.2f}")
    elif pilihan == 3:
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        luas = 0.5 * a * t
        print(f"Luas segitiga (alas={a}, tinggi={t}) = {luas}")
    else:
        print("Pilihan tidak valid.")
except ValueError:
    print("Input harus angka.")