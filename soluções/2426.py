from bisect import bisect_right, insort
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        chave = []
        total = 0
        
        for idx in range(len(nums1)):
            atual = nums1[idx] - nums2[idx]
            
            limite = atual + diff
            total += bisect_right(chave, limite)
            
            insort(chave, atual)
        
        return total
