import random


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(random.random() * 100))
    print(arr)
    bubble_sort(arr)
    print(arr)
