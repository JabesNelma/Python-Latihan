# Kalkulator Sederhana
print("=== KALKULATOR SEDERHANA ===")

while True:
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        op = input("Pilih operator (+, -, *, /): ")

        if op == '+':
            hasil = a + b
        elif op == '-':
            hasil = a - b
        elif op == '*':
            hasil = a * b
        elif op == '/':
            if b == 0:
                print("Error: Pembagian dengan nol!")
                continue
            hasil = a / b
        else:
            print("Operator tidak valid!")
            continue

        print(f"Hasil: {a} {op} {b} = {hasil}")
        break
    except ValueError:
        print("Input harus berupa angka! Silakan ulang.")