#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:        # base case: PIN sudah sepanjang yang diminta
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:
        # supaya angka tidak berulang: sebelum rekursi, cek dulu
        # if angka in hasil: continue  # kalau sudah pernah dipakai, lewati
        buat_pin(panjang, hasil + angka)

buat_pin(3)