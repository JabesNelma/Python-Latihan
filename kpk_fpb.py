# KPK dan FPB
import math

print("=== KPK DAN FPB ===")

try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    if a <= 0 or b <= 0:
        print("Bilangan harus positif.")
    else:
        fpb = math.gcd(a, b)
        kpk = abs(a * b) // fpb
        print(f"FPB dari {a} dan {b} = {fpb}")
        print(f"KPK dari {a} dan {b} = {kpk}")
except ValueError:
    print("Input harus bilangan bulat.")