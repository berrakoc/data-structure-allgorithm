from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Test
solution = Solution()

# Test case 1: List with duplicates
nums1 = [1, 2, 3, 4, 5, 2]
print(solution.hasDuplicate(nums1))  # Output: True

# Test case 2: List without duplicates
nums2 = [1, 2, 3, 4, 5]
print(solution.hasDuplicate(nums2))  # Output: False

# Test case 3: Empty list
nums3 = []
print(solution.hasDuplicate(nums3))  # Output: False

# Test case 4: List with one element
nums4 = [1]
print(solution.hasDuplicate(nums4))  # Output: False
