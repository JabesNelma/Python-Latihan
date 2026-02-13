# Frekuensi Huruf
print("=== FREKUENSI HURUF ===")

teks = input("Masukkan teks: ")
freq = {}
for huruf in teks.lower():
    if huruf.isalpha():
        freq[huruf] = freq.get(huruf, 0) + 1

print("Frekuensi kemunculan huruf:")
for huruf, jumlah in sorted(freq.items()):
    print(f"{huruf}: {jumlah}")