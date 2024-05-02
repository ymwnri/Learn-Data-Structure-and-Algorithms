def selection_sort(my_list):

    # Define length
    list_length = len(my_list)

    # Traverse through all array elements
    for i in range(list_length - 1):
        
        # lowest element in the unsorted array
        lowest = my_list[i]
        index = i

        # Find the minimum el list_lengtement in remaining unsorted array
        for j in range(i + 1):

            # If found, update the minimum element
            if my_list[j] < lowest:
                index = j
                lowest = my_list[j]
                
            # Swap the found minimum element with the first element
            my_list[i], my_list[index] = my_list[index], my_list[i]
        return my_list

        
       