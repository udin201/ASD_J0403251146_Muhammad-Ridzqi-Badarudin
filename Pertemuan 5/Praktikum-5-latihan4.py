#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:             # base case: panjang sudah n → 1 kombinasi jadi
        print(hasil)
        return

    kombinasi(n, hasil + "A")       # pilihan 1 untuk tiap posisi
    kombinasi(n, hasil + "B")       # pilihan 2 untuk tiap posisi
    # jumlah output = 2^n, karena tiap posisi selalu punya 2 pilihan (A/B) sampai n posisi

kombinasi(2)