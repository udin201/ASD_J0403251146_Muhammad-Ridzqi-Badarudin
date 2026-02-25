#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0:                 # berhenti saat n=0 (a^0 = 1)
        return 1
    # Recursive case
    return a * pangkat(a, n - 1) # panggil lagi dengan n-1 (dibuat makin kecil biar nyampe base case)

print(pangkat(2, 4))  # Output: 16  # urutannya: pangkat(2,4)->...->pangkat(2,0), lalu balik sambil dikali 2