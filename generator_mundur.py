# Generator Hitung Mundur
print("=== HITUNG MUNDUR ===")

def hitung_mundur(n):
    while n > 0:
        yield n
        n -= 1

try:
    n = int(input("Masukkan angka awal: "))
    if n <= 0:
        print("Angka harus positif.")
    else:
        print("Hitung mundur:")
        for angka in hitung_mundur(n):
            print(angka, end=' ')
        print()
except ValueError:
    print("Input harus bilangan bulat.")