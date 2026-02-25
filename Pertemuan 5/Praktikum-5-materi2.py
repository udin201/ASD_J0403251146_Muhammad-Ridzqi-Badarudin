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


    if n == 0:
        return
    print(n)
    hitung(n-1)