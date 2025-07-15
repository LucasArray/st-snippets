class Solution:
    def binary_search(self, arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

# Example usage:
sorted_array = [2, 3, 4, 10, 40]
target = 10
solver = Solution()
result = solver.binary_search(sorted_array, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in array.")