### 189. Rotate Array
### https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&id=top-interview-150

"""
Runtime | 229 ms
Beats |44.68%
Memory | 28.1 MB
Beats| 8.64%
"""

"""
    My approach for this solution was to achieve an in place solve by reversing the string initially,
    then reversing the front of the reversed string that would have been the n number of rotated positions,
    then rotating the remainder of the string so the enitre array is in order as required.
"""
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_array_part(arr, start_index, end_index):
            arr[start_index:end_index+1] = arr[start_index:end_index+1][::-1]
        n = len(nums)
        diffK = k % len(nums)
        reverse_array_part(nums, 0, n)
        reverse_array_part(nums, 0, diffK-1)
        reverse_array_part(nums, diffK, n)

"""
    The following code is a non-in-place version of the solution for the problem.
    The idea behind this is very simply, taking the back portion of the original array which contains the k
    positions to be rotated, and putting that section in front of the rest of the array in a new array.
"""      
"""
    def rotate(self, nums, k) -> None:
        firstHalf = nums[:len(nums)-k]
        backHalf = nums[len(nums)-k:]
        retArr = backHalf+firstHalf
        return retArr
"""
        
sol = Solution()

print(sol.rotate([1,2,3,4,5,6,7], 3))

        