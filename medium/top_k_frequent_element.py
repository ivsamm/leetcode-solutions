from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_count = Counter(nums)
        sorted_res = dict(sorted(res_count.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_res.keys())[:k]
    
if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))