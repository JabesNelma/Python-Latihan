# Error Handling (Pembagian)
print("=== PEMBAGIAN DENGAN ERROR HANDLING ===")

try:
    a = float(input("Masukkan pembilang: "))
    b = float(input("Masukkan penyebut: "))
    hasil = a / b
except ZeroDivisionError:
    print("Error: Penyebut tidak boleh nol!")
except ValueError:
    print("Error: Input harus angka!")
else:
    print(f"Hasil: {a} / {b} = {hasil}")
finally:
    print("Terima kasih telah menggunakan program.")