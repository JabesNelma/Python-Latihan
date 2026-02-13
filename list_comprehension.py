# List Comprehension
print("=== LIST COMPREHENSION ===")

try:
    n = int(input("Batas atas bilangan: "))
    if n <= 0:
        print("Batas harus positif.")
    else:
        kuadrat = [x**2 for x in range(1, n+1)]
        genap = [x for x in range(1, n+1) if x % 2 == 0]
        ganjil = [x for x in range(1, n+1) if x % 2 != 0]

        print(f"Kuadrat 1-{n}: {kuadrat}")
        print(f"Bilangan genap 1-{n}: {genap}")
        print(f"Bilangan ganjil 1-{n}: {ganjil}")
except ValueError:
    print("Input harus bilangan bulat.")