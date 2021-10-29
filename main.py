def insertionSort(array):
    """
    A function that takes in an array of integers and returns a sorted version of that array using the insertion sort
    algorithm.
    """
    for idx in range(1, len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            swap(idx, idx - 1, array)
            idx -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
