from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            1. Start from the end of both arrays.
            2. Compare the elements and place the larger element at the end of the first array.
            3. Move the pointers and repeat until all elements are merged.
        """
        p1 = m - 1
        p2 = n - 1
        i = (n + m - 1)

        while p2 >= 0:
            n1 = nums1[p1]
            n2 = nums2[p2]
            if p1 >= 0 and n1 > n2:
                p1 -= 1
                nums1[i] = n1
            else: 
                p2 -= 1
                nums1[i] = n2
            i -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)

print(nums1)
