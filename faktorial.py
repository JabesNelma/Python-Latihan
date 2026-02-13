# Faktorial
print("=== FAKTORIAL ===")

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

try:
    n = int(input("Masukkan bilangan (non-negatif): "))
    if n < 0:
        print("Faktorial hanya untuk bilangan non-negatif.")
    else:
        print(f"{n}! = {faktorial(n)}")
except ValueError:
    print("Input harus bilangan bulat.")