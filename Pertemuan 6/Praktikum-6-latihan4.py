def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left_sorted, right_sorted):
    return

#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?

#Jawaban: 
#1. Kondisi berhenti rekursi. Di kode ini: len(data) <= 1 artinya list 0/1 elemen sudah terurut, jadi langsung dikembalikan.
#2. Karena merge sort memakai strategi divide and conquer: pecah list jadi dua bagian, urutkan masing-masing bagian dengan cara yang sama (rekursif), lalu gabungkan.
#3. Untuk menggabungkan dua list yang sudah terurut (left_sorted dan right_sorted) menjadi satu list terurut.