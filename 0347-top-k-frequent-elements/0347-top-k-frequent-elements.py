from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        count = Counter(nums)
        
        # Get the k most common elements (returns a list of tuples: (element, frequency))
        return [item[0] for item in count.most_common(k)]
