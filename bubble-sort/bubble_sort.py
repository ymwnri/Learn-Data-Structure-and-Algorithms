# Bubble sort
def bubble_sort(my_list):
    
    # Traverse through all elements in the list
    for i in range(len(my_list)-1):

        # Traverse the list from 0 to n-i-1
        for j in range(len(my_list)-1-i):

            # Swap if the element found is greater
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

# Test
print(bubble_sort([4, 3, 7, 1, 5]))

def bubble_sort_2(my_list):
    
    # Define list length
    list_length = len(my_list)

    # check if the list is already sorted
    is_sorted = False

    while not is_sorted:

        # set is_sorted to True
        is_sorted = True

        for i in range(list_length-1):

            # if the element is greater than the next element
            if my_list[i] > my_list[i+1]:

                # swap the elements
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

                # set is_sorted to False
                is_sorted = False
        
        # decrement the list length
        list_length -= 1
    return my_list