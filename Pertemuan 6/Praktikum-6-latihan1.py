def insertion_sort(data):
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1

        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j = 1
    
    data[j + 1] = key

    return data

#Soal:
#1. Mengapa perulangan dimulai dari indeks 1?
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?

#Jawaban:
#1. Karena pada insertion sort, elemen indeks 0 dianggap sudah “sorted” (sub-list terurut paling kecil).
#2. key menyimpan nilai elemen yang sedang ingin ditempatkan pada posisi yang benar.
#3. Karena jumlah langkah pergeseran tidak diketahui di awal—bergantung pada berapa banyak elemen di kiri yang lebih besar dari key.
#4. Terjadi perbandingan (data[j] > key) lalu pergeseran/shift ke kanan (data[j+1] = data[j]) sambil j mundur (j -= 1). Ini membuka “slot” untuk menaruh key.