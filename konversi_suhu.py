# Konversi Suhu
print("=== KONVERSI SUHU ===")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")

try:
    pilihan = int(input("Pilih menu (1/2): "))
    if pilihan == 1:
        c = float(input("Masukkan suhu Celcius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    elif pilihan == 2:
        f = float(input("Masukkan suhu Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")
    else:
        print("Pilihan tidak valid.")
except ValueError:
    print("Input harus angka.")