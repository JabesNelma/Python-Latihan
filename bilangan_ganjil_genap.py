# Cek Ganjil Genap
print("=== CEK GANJIL GENAP ===")

try:
    n = int(input("Masukkan bilangan: "))
    if n % 2 == 0:
        print(f"{n} adalah bilangan genap.")
    else:
        print(f"{n} adalah bilangan ganjil.")
except ValueError:
    print("Input harus bilangan bulat.")