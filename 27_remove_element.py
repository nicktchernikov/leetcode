from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        k = 0
        for p2 in range(len(nums)):
            if (nums[p2] != val):
                nums[p1] = nums[p2]
                p1 += 1
                k += 1
        # Alternate 2-pointer solution (a bit faster, apparently)  
        # p2 = 0
        # while p2 < len(nums):
        #     if nums[p2] == val:
        #         p2 += 1
        #     else:
        #         nums[p1] = nums[p2]
        #         p1 += 1
        #         p2 += 1
        #         k += 1
        return k
    
# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

solution = Solution()
k = solution.removeElement(nums, val)

print(nums, k)