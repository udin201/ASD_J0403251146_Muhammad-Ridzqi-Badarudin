#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:      # kalau sudah elemen terakhir, ya itu “maks”-nya
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)  # cari maks dari sisa elemen setelah index
    if data[index] > maks_sisa:             # bandingin elemen sekarang vs maks_sisa
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))  # hasil akhir muncul saat proses balik ke atas selesai