# Bubble Sort
- First value > second value
    - Swap
- Second value greater than the first value
    - Do nothing
```python
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
```

## Complexity
- Worst case: O(n^2)
- Best case - not improved version: Omega(n^2)
- Best case - improved version: Omega(n)
- Average case: Theta(n^2)
- Doesn't perform well with highly unsorted large lists
- Performs well:
    - large sorted/almost sorted lists
    - small lists