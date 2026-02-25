#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Implementasi : Rekursif
#Case : Menghitung jumlah dalam baris
#base case => sampai akhir list
#====================================

def jumlah_list(n, index=0): 
    if index == len(n):
        return 0
    
    return n [index] + jumlah_list(n, index+1)

print(jumlah_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))