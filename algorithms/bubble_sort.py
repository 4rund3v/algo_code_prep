


def bubble_sort(arr):
    """
    largest item is in the right position
    O (n^2)
    """
    i = 0
    for i in range(len(arr)):        
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([30,123,1,2,4,1,4,56,71,69, 65]))
