def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and ...:
            data[j + 1] = data[j]
            j -= 1

    ...
    return data

#Jawaban:
#1
def insertion_sort_ascending(data):
    # Kondisi ascending: geser elemen yang lebih besar dari key
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data

#2
def insertion_sort_descending(data):
    # Kondisi descending: geser elemen yang lebih kecil dari key
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data