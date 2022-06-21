class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        l = len(nums1)
        i = (l+1)//2
        if l%2!=0:
            return nums1[i-1]
        return (nums1[i-1]+nums1[i])/2
