from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (n1 + n2 + 1) // 2 - mid1

            left1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            right1 = float('inf') if mid1 == n1 else nums1[mid1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            right2 = float('inf') if mid2 == n2 else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1

        raise ValueError("Entrada inválida: arrays não estão ordenados ou possuem formato inesperado.")
