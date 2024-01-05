def quickSort(arr, low, high):
    if (low >= high):
        return arr
    # Setting the last element as the pivot
    pivot = arr[high]

    start, end = low, high
    while (start <= end):
        # Also a reason why if its already sorted, it will not swap
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if (start <= end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Now my pivot is at the correct index, sort the two halves now
    quickSort(arr, low, end)
    quickSort(arr, start, high)
    return arr


unsorted_list = [3, 7, 12, 24, 36, 42]
sorted_list = quickSort(unsorted_list, 0, len(unsorted_list) - 1)
print("Sorted list:", sorted_list)

# OR 

from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], list[less_than_pointer]))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)    
  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)