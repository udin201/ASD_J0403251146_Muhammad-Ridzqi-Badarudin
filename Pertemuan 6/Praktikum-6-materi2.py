#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Insertion  sort dengan tracing
#====================================

def insertion_sort(data):
    
    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)

    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang di sisipkan
        j = i-1 #index elemen terakhir di bagian kiri

        print("Iterasi ke- ", i)
        print("Nilai Key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i+1:])

        #geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("="*50)
    return data
angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", insertion_sort(angka))
        