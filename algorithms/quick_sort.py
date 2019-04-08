def quick_sort(arr, first, last):

    # only run till first index < last

    if first < last:
        split_index = partition(arr, first, last)
        quick_sort(arr, first, split_index - 1)
        quick_sort(arr, split_index+1, last)


def partition(arr, first, last):
    pivot = arr[first]

    leftmark = first + 1
    rightmark = last

    # print(f'before done: leftmarker: {arr[leftmark]}, rightmarker: {arr[rightmark]}')
    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1

        while rightmark >= leftmark and arr[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            # print(f'else: l,r: {leftmark}, {rightmark}')
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


if __name__ == '__main__':
    array = [7, 8, 2, 5, 1, 9]
    first = 0
    last = len(array) - 1
    # print(partition(array, first, last))
    quick_sort(array, first, last)
    print(array)
