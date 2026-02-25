#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
#input 3
# Masuk 1 -2 - 3
# Keluar 3 - 2 - 1
#====================================

def hitung(n):
    print("Masuk", n)
    if n == 0:
        print("Basw case tercapai, berhenti")
        return 1
    hasil = n * hitung(n-1)
    print("Keluar", n)
    return hasil

print("======Program hitung======")
hitung(3)