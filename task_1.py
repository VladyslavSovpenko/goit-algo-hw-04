import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def timsort(arr):
    return sorted(arr)

def measure_time(sort_func, data):
    timer = timeit.Timer(lambda: sort_func(data.copy()))
    return timer.timeit(number=10)

data_sizes = [100, 1000, 10000]
datasets = {size: [random.randint(0, 10000) for _ in range(size)] for size in data_sizes}

for size, data in datasets.items():

    time_insertion = measure_time(insertion_sort, data)
    print(f"Insertion Sort: {time_insertion:.6f} секунд")

    time_merge = measure_time(merge_sort, data)
    print(f"Merge Sort: {time_merge:.6f} секунд")

    time_timsort = measure_time(timsort, data)
    print(f"Timsort: {time_timsort:.6f} секунд")
