class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1=list(filter(lambda x : x!=0,nums1))
        loop_run=len(nums1)-m
        for i in range(loop_run):
            nums1.remove(0)
         
        if n>0:
            for num in nums2:
                nums1.append(num) 
        nums1.sort()
       
