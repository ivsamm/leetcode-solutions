# 217.Contains Duplicate
from  typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        return True if len(nums) != len(set_nums) else False
    

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))