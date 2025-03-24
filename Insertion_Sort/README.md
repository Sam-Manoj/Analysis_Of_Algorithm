# Insertion Sort

## Introduction
1) Insertion sort is a very simple method to sort numbers in an ascending or descending order. This method follows the **incremental method**.
2) An element which is to be 'inserted' in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, 
   **insertion sort**.

## Algorithm
**STEP 1** − If it is the first element, it is already sorted. return 1;

**STEP 2** − Pick next element

**STEP 3** − Compare with all elements in the sorted sub-list

**STEP 4** − Shift all the elements in the sorted sub-list that is greater than the value to be sorted

**STEP 5** − Insert the value

**STEP 6** − Repeat until list is sorted


## Pseudocode
```
InsertionSort(A, n):
    for j ← 2 to n:
        key ← A[j]  // Pick the first element of the unsorted part
        i ← j - 1   // Set i to the last index of the sorted part
        while i > 0 and A[i] > key:
            A[i+1] ← A[i]  // Shift elements to the right to create space
            i ← i - 1  // Move left in the sorted part
        A[i+1] ← key  // Insert the key at the correct position
```

## Explanation of Pseudocode
1. **for j ← 2 to n:**
   - Iterate through each element of the array starting from the second element.
2. **key ← A[j]:**
   - Store the current element (key) that needs to be inserted in the sorted part.
3. **i ← j - 1:**
   - Start comparing the key with the elements in the sorted part, moving from right to left.
4. **while i > 0 and A[i] > key:**
   - Continue shifting elements to the right until we find the correct position for the key.
5. **A[i+1] ← A[i]:**
   - Move the larger element one step to the right.
6. **i ← i - 1:**
   - Move to the next element on the left.
7. **A[i+1] ← key:**
   - Place the key in its correct sorted position.

## Time Complexity
- **Best Case (Already Sorted):** O(n)
- **Average Case:** O(n²)
- **Worst Case (Reverse Sorted):** O(n²)

## Space Complexity
- **O(1)** (In-place sorting algorithm)

## Real-World Applications
1. **Sorting Playing Cards** – The method players use to arrange cards in their hand.
2. **Small Data Sets** – Due to its simplicity, it's preferred when dealing with a small number of elements.
3. **Online Sorting** – When data is continuously received and needs to be sorted dynamically, such as real-time ranking systems.
4. **Almost Sorted Data** – Works efficiently if the dataset is nearly sorted.

## Advantages
- Simple and easy to implement.
- Performs well with small or nearly sorted datasets.
- Works in-place, requiring no additional memory.

## Disadvantages
- Inefficient for large datasets due to O(n²) complexity.
- Slower compared to advanced sorting algorithms like Merge Sort or Quick Sort.

