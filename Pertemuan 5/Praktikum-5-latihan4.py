#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)