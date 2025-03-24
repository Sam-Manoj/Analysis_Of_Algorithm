def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key < array[j]:
            array[j+1]=array[j]
            j-=1
            array[j+1]=key
            
array= list(map(int,input("Enter The numbers(Should be separated by spaces").split()))  
insertion_sort(array)  
print("Sorted array:",array)

# 1: Define a function named 'insertion_sort' that takes an array as input.
# 2: Start a loop from index 1 to the last index of the array.
# 3: Store the current element in a variable 'key'.
# 4: Set 'j' to the index before 'i' (to compare with previous elements).
# 5: Start a while loop to shift elements greater than 'key' to the right.
# 6: Move the larger element one position ahead.
# 7: Decrement 'j' to compare with the previous element.
# 8: Place 'key' in the correct position after shifting.
# 10: Take user input, split it into a list of strings, convert each string to an integer, and store it in 'array'.
# 11: Call the 'insertion_sort' function to sort the array.
# 12: Print the sorted array.
