# Cek Bilangan Prima
print("=== CEK BILANGAN PRIMA ===")

try:
    n = int(input("Masukkan bilangan: "))
    if n <= 1:
        print(f"{n} bukan bilangan prima.")
    else:
        prima = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prima = False
                break
        print(f"{n} adalah {'bilangan prima' if prima else 'bukan bilangan prima'}.")
except ValueError:
    print("Input harus bilangan bulat.")