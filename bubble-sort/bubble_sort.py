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