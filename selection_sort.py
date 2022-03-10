def selection_sort(array):
    # step 1: loop from the beginning of the array to the second to last item
    current_index = 0
    while current_index < len(array) - 1:
        # step 2: save a copy of the current_index
        min_index = current_index
        # step 3: loop through all indexes that proceed the current_index
        i = current_index + 1
        while i < len(array):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at min_index, update min_index
            #           with the new lowest value index
            if array[i][1] < array[min_index][1]:
                # update min_index with the new lowest value index
                min_index = i
            i += 1
        # step 5: if min_index has been updated, swap the values at min_index and current_index
        if min_index != current_index:
            temp = array[current_index]
            array[current_index] = array[min_index]
            array[min_index] = temp
        current_index += 1
    return array


if __name__ == "__main__":
    array = [(12, 0), (15, 10), (9, 1), (2, 3), (13, 14), (4, 5)]
    selection_sort([64, 25, 12, 22, 11])
