# Dictionary Comprehension
print("=== DICTIONARY COMPREHENSION ===")

try:
    n = int(input("Batas atas bilangan: "))
    if n <= 0:
        print("Batas harus positif.")
    else:
        kuadrat_dict = {x: x**2 for x in range(1, n+1)}
        print(f"Dictionary (x: x^2) 1-{n}:")
        for k, v in kuadrat_dict.items():
            print(f"{k}: {v}")
except ValueError:
    print("Input harus bilangan bulat.")