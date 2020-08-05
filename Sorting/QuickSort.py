# implementation of quick sort

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr

def quickSortHelper(arr, low, high):
    if low < high:
        # partition the array on the basis of pivot
        # at the end of this call the pivot is inserted
        # into its correct position in the array
        pivot_idx = partition(arr, low, high)
        # call the helper to sort the sub-arrays
        # sorting the elements to the left of the pivot element
        quickSortHelper(arr, low, pivot_idx - 1)
        # sorting the elements to the right of the pivot element
        quickSortHelper(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    # this function partitions the array on the basis of the pivot element
    # consider the pivot to be the last element in the array
    pivot = arr[high]

    # pointer which keeps track of the numbers smaller than the pivot
    # if a number which is less than the pivot is discovered at j
    # then i is incremented and the values are swapped.
    i = low - 1
    for j in range(low, high):
        # when an element < pivot is found
        if arr[j] < pivot:
            # i is incremented to indicate the position where the smaller number
            # is to be placed. The numbers are then swapped
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # at the end the pivot is placed into its correct position in the array
    # i before increment is the position at which the most recent number which was
    # found to be < pivot was placed. i + 1 holds an element >= pivot. We swap the pivot
    # and this element to place the pivot correctly in the array.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # return the index of the pivot in the array
    return (i + 1)

if __name__ == "__main__":
    print(quickSort([2, 4, 7, 5, 9, 3, 1]))



