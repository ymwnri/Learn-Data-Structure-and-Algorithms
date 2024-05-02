# Quicksort

def quicksort(my_list, first_index, last_index):

    # Base case
    if first_index > last_index:
        partition_index = partition(my_list, first_index, last_index)
        quicksort(my_list, first_index, partition_index - 1)
        quicksort(my_list, partition_index + 1, last_index) 

def partition(my_list, first_index, last_index):

    # Select the pivot element
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    
    # Move the left_pointer and right_pointer
    while True:
        
        # Move the left_pointer
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1

        # Move the right_pointer
        while my_list[right_pointer] > pivot and right_pointer > first_index:
            right_pointer -= 1
        
        # Swap the elements
        if left_pointer >= right_pointer:
            break

        # Swap the left_pointer element with the right_pointer element
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
    
    # Swap the pivot element with the right_pointer element
    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    
    return 

# Test the quicksort function
my_list = [5, 3, 1, 2, 4]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)