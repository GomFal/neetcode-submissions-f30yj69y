class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A)+len(B)
        half = total//2

        l, r = 0, len(A)-1 
        
        # We only execute binary search on the smallest array for efficiency

        while True:
            i = (l+r)//2        # Smallest array border
            j = half - i - 2    # So that the left partition sums up to the half of the elements

            Aleft = A[i] if i >= 0 else float("-infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            # Check whether the partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                # The partitions are correct. Now we check if they are even or odd
                if total % 2:
                    return min(Aright, Bright)
                return ((max(Aleft, Bleft) + min(Aright, Bright))/2)
            
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            


        
        

    

            
        
        
        



            



        
                

              