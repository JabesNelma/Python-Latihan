# Kalkulator BMI
print("=== KALKULATOR BMI ===")

try:
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))
    if berat <= 0 or tinggi <= 0:
        print("Berat dan tinggi harus positif.")
    else:
        bmi = berat / (tinggi ** 2)
        print(f"BMI Anda: {bmi:.2f}")
        if bmi < 18.5:
            print("Kategori: Kurang berat badan")
        elif bmi < 25:
            print("Kategori: Normal")
        elif bmi < 30:
            print("Kategori: Kelebihan berat badan")
        else:
            print("Kategori: Obesitas")
except ValueError:
    print("Input harus angka.")