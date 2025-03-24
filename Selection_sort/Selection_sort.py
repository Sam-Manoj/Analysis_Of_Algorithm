def Selection_sort(array):
    for i in range (1,len(array)-1):
         j=i
         for key in range(i+1,len(array)):
             if (array[key]<array[j]):
                 j=key
                 array[i], array[j] = array[j], array[i] 
array= list(map(int,input("Enter The numbers(Should be separated by spaces)").split()))  
Selection_sort(array)  
print("Sorted array:",array)

# 1. def Selection_sort(array):  
#    → Defines the function `Selection_sort` that takes a list (`array`) as input and sorts it using the Selection Sort algorithm.

# 2. for i in range(len(array) - 1):  
#    → Outer loop runs from the first element (`i = 0`) to the second last element (`i = len(array) - 2`), ensuring all elements are sorted except the last one.

# 3. j = i  
#    → Assumes the current index `i` holds the smallest element in the unsorted portion of the array.

# 4. for key in range(i + 1, len(array)):  
#    → Inner loop iterates through the remaining unsorted portion to find the smallest element.

# 5. if array[key] < array[j]:  
#    → Compares each element (`array[key]`) with the current minimum (`array[j]`). If a smaller element is found, `j` is updated.

# 6. j = key  
#    → Updates `j` to store the index of the newly found smallest element.

# 7. array[i], array[j] = array[j], array[i]  
#    → Swaps the smallest element found (`array[j]`) with the element at index `i`, placing it in its correct sorted position.

# 8. array = list(map(int, input("Enter the numbers (separated by spaces): ").split()))  
#    → Takes user input as a space-separated string.
#    → Uses `split()` to separate individual numbers.
#    → Converts them into integers using `map(int, ...)`.
#    → Stores them in a list named `array`.

# 9. Selection_sort(array)  
#    → Calls the `Selection_sort` function to sort the user-provided list.

# 10. print("Sorted array:", array)  
#     → Prints the sorted list after applying Selection Sort.        
                 