#Buat program dengan menggunakan algoritma insertion sort
#Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort_with_trace(data):
    """
    Tracing data = [5, 2, 4, 6, 1, 3]
    Jawaban:
    - Setelah i=1: [2, 5, 4, 6, 1, 3]
    - Setelah i=3: [2, 4, 5, 6, 1, 3]
    - Pergeseran pada i=4: 4 kali (6,5,4,2 digeser)
    """
    data = data[:]  # copy biar tidak mengubah list asli
    print("Awal:", data)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        shifts = 0

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            shifts += 1

        data[j + 1] = key
        print(f"i={i}, key={key}, shifts={shifts} -> {data}")

    return data

if __name__ == "__main__":
    insertion_sort_with_trace([5, 2, 4, 6, 1, 3])
