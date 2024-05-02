
def insertion_sort(my_list):
    # Traverse through 1 to len(arr)
    for i in range(1, len(my_list)):

        # Store number to be ordered
        number_ordered = my_list[i]

        # Move elements of arr[0..i-1], that are greater than number_ordered, to one position ahead of their current position
        j = i - 1

        # While j is greater than or equal to 0 and the number_ordered is less than the element at index j
        while j >= 0 and number_ordered < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1

        # Insert the number_ordered at its correct position
        my_list[j + 1] = number_ordered
    
    # Return the sorted list
    my_list[j + 1] = number_ordered