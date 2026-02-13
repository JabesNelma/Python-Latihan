# Konversi Biner
print("=== KONVERSI BILANGAN ===")

print("1. Desimal ke Biner")
print("2. Biner ke Desimal")

try:
    pilihan = int(input("Pilih menu (1/2): "))
    if pilihan == 1:
        des = int(input("Masukkan bilangan desimal: "))
        biner = bin(des)[2:]
        print(f"{des} dalam biner = {biner}")
    elif pilihan == 2:
        bin_str = input("Masukkan bilangan biner: ")
        desimal = int(bin_str, 2)
        print(f"{bin_str} dalam desimal = {desimal}")
    else:
        print("Pilihan tidak valid.")
except ValueError:
    print("Input tidak valid.")