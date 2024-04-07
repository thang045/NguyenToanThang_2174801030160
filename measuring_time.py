import random
import time


def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]


def swap_index(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def interchange_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swap_index(arr, i, j)
        # print(f"Loop {i + 1}: {arr}")
    return arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                swap_index(arr, j, j-1)
        # print(f"Loop {i}: {arr} \n")
    return arr


def insertion_sort(arr, n):
    i = 1
    for i in range(i, n, 1):
        x = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > x:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = x
        # print(f"Loop {i}: {arr}\n")


def selection_sort(arr, n):
    for i in range(0, n-1, 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            swap_index(arr, min_index, i)
        # print(f"Loop {i}: {arr} \n")


def quick_sort(arr, left, right):
    if left >= right:
        return
    x = arr[(left+right)//2]
    i = left
    j = right
    while i < j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i <= j:
            swap_index(arr, i, j)
            i += 1
            j -= 1
    if left < i:
        quick_sort(arr, left, j)
    if i < right:
        quick_sort(arr, i, right)


def time_sorting_algorithms(size):
    random_list = generate_random_list(size)
    algorithms = [
        ("Interchange Sort", interchange_sort, random_list.copy()),
        ("Bubble Sort", bubble_sort, random_list.copy()),
        ("Insertion Sort", insertion_sort, random_list.copy(), size),
        ("Selection Sort", selection_sort, random_list.copy(), size),
        ("Quick Sort", quick_sort, random_list.copy(), 0, len(random_list) - 1)
    ]
    shortest_time = float('inf')
    fastest_algorithm = None
    for algorithm_name, algorithm_func, *args in algorithms:
        print(f"Running {algorithm_name}...")
        start_time = time.time()
        algorithm_func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{algorithm_name} Execution Time: {execution_time:.6f} seconds")
        print()

        if execution_time < shortest_time:
            shortest_time = execution_time
            fastest_algorithm = algorithm_name

    print(f"The fastest algorithm is {fastest_algorithm} with an execution time of {shortest_time:.6f} seconds.")


if __name__ == '__main__':
    size = int(input("Enter the size of the list: "))
    time_sorting_algorithms(size)

