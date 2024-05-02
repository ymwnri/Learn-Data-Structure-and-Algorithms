# Merge sort

def merge_sort(my_list):

    # Check if the length of the list is greater than 1
    if len(my_list) > 1:

        # Find the middle of the list
        mid = len(my_list) // 2

        # Divide the list elements into two halves
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursively sort the two halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):

            # If the element in the left list is less than the element in the right list
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            
            # If the element in the right list is less than the element in the left list
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
    
        # Check if any element was left
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

# Test the function
my_list = [6, 2, 9, 7, 4, 8]
merge_sort(my_list)
print(my_list)