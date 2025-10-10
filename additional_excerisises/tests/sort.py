class Sort:
    """A collection of sorting algorithms"""

    def bubble(self, arr):
        """
        Implements bubble sort with O(n²) time complexity. Compares adjacent elements
        and swaps if out of order, repeatedly passing through array until sorted.

        LIMITATIONS: Modifies original array in-place without copying. Fails on empty
        arrays (IndexError on arr[0]). No validation for non-comparable types (strings
        mixed with integers will crash). Doesn't handle None values. Only works with
        lists, not tuples or other iterables. No parameter for reverse sorting.

        TODO: Add empty array check before accessing arr[0]
        TODO: Create copy of array before sorting to preserve original
        TODO: Add reverse parameter for descending order support
        """
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge(self, arr):
        """
        Divide-and-conquer algorithm splitting array recursively then merging sorted halves.
        Time: O(n log n), Space: O(n) for temporary arrays.

        CRITICAL FLAWS: Crashes on
        single-element arrays due to mid calculation creating infinite recursion when
        mid equals left. No handling for None/null values which cause comparison errors.
        Assumes all elements are comparable; mixing types raises TypeError. Creates many
        temporary lists causing high memory usage. No stability guarantee maintained.

        TODO: Fix base case to handle len(arr) <= 1 instead of just <= 0
        TODO: Add type validation to prevent mixed-type comparison crashes
        TODO: Optimize memory by using in-place merging instead of new lists
        """
        if len(arr) <= 0:
            return arr

        mid = len(arr) // 2
        left = self.merge(arr[:mid])
        right = self.merge(arr[mid:])

        return self._merge_halves(left, right)

    def _merge_halves(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick(self, arr):
        """
        Efficient sorting using pivot partitioning with average O(n log n) complexity.
        Selects last element as pivot (poor choice for sorted/reverse-sorted data causing
        O(n²) worst case).

        BUGS: Returns new list instead of sorting in-place unlike
        bubble method, creating inconsistent API. Fails on arrays with duplicate values
        due to missing equal-to-pivot handling in partitions. No random pivot means
        predictable poor performance on already-sorted data. Stack overflow risk on large arrays.

        TODO: Implement random pivot selection to avoid O(n²) on sorted data
        TODO: Handle duplicates by adding middle partition for pivot-equal values
        TODO: Make API consistent - either all in-place or all return new lists
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x > pivot]

        return self.quick(left) + [pivot] + self.quick(right)
