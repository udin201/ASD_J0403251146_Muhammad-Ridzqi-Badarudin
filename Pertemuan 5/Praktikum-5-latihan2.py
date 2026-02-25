#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    if n == 0:                  # base case: paling bawah
        print("Selesai")
        return                  # mulai “balik” ke atas (unwinding)

    print("Masuk:", n)          # dicetak sebelum turun rekursi: 3,2,1
    countdown(n - 1)            # recursive call: turun sampai n=0
    print("Keluar:", n)         # dicetak setelah balik, jadi kebalik: 1,2,3 (yang paling dalam keluar duluan)

countdown(3)