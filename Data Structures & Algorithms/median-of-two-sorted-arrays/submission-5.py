class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        total = len(nums1) + len(nums2)
        half = total//2

        l, r = 0, len(A)-1

        while True: # We know there is a median 100%
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            # Check if the slices are correct
            if Aleft  <= Bright and Bleft <= Aright:
                # Correct
                # Odd or even?
                if total % 2:
                    return min(Aright, Bright)
                else:
                    res = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                    return res
                    
            elif Aleft > Bright:
                r = i - 1
            elif Aright < Bleft:
                l = i + 1
            



        
                

              