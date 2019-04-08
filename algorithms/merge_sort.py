def merge_sort(arr):

    # base case:
    # if len(arr) <= 1:
    #     print(arr)
    #     return arr

    # recursive case
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(f'Before recursive call: {arr}')
        merge_sort(left_half)
        merge_sort(right_half)

        # now start merging
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        print(f'mid merging {arr}')

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f'Merging: {arr}')


if __name__ == "__main__":
    arr = [5, 2, 9, 8, 10, 12, 1]
    # print(arr)
    merge_sort(arr)
    print(arr)
