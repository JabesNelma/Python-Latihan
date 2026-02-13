# Menggabung Dua Dictionary
print("=== GABUNG DICTIONARY ===")

dict1 = {}
dict2 = {}

print("Masukkan dictionary pertama:")
try:
    n1 = int(input("Jumlah pasangan key-value: "))
    for _ in range(n1):
        k = input("Key: ")
        v = input("Value: ")
        dict1[k] = v

    print("Masukkan dictionary kedua:")
    n2 = int(input("Jumlah pasangan key-value: "))
    for _ in range(n2):
        k = input("Key: ")
        v = input("Value: ")
        dict2[k] = v

    gabung = {**dict1, **dict2}
    print(f"Dictionary 1: {dict1}")
    print(f"Dictionary 2: {dict2}")
    print(f"Gabungan: {gabung}")
except ValueError:
    print("Input jumlah harus angka.")