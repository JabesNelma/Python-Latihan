# Cek Palindrom
print("=== CEK PALINDROM ===")

teks = input("Masukkan kata/kalimat: ")
bersih = teks.lower().replace(" ", "")
if bersih == bersih[::-1]:
    print(f"'{teks}' adalah palindrom.")
else:
    print(f"'{teks}' bukan palindrom.")