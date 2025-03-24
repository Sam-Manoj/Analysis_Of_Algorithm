# Selection Sort

## Introduction
Selection sort is a simple sorting algorithm. This sorting algorithm, like insertion sort, is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

## Algorithm
**STEP 1** : Set MIN to location 0.
**STEP 2** : Search the minimum element in the list.
**STEP 3** : Swap with value at location MIN.
**STEP 4** : Increment MIN to point to next element.
**STEP 5** : Repeat until the list is sorted.

## Pseudocode
```
Algorithm: Selection-Sort (A)
for i← 1 to n-1 do
  min j ←i;
  min x ← A[i]
  for j ←i + 1 to n do
    if A[j] < min x then
      min j ← j
      min x ← A[j]
  A[min j] ← A [i]
  A[i] ← min x
```
# Time Complexity

Best-case: **O(n²)** , best case occurs when the array is already sorted. (where n is the number of integers in an array)

Average-case: **O(n²)**, the average case arises when the elements of the array are in a disordered or random order, without a clear ascending or descending pattern.

Worst-case: **O(n²)**, The worst-case scenario arises when we need to sort an array in ascending order, but the array is initially in descending order.
