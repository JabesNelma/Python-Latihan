# Deret Fibonacci
print("=== DERET FIBONACCI ===")

try:
    n = int(input("Masukkan jumlah suku Fibonacci: "))
    if n <= 0:
        print("Jumlah suku harus positif.")
    else:
        a, b = 0, 1
        deret = []
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b
        print(f"{n} suku pertama Fibonacci: {deret}")
except ValueError:
    print("Input harus bilangan bulat.")