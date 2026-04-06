class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # A deque can be used to store the max elements at the left of the deque
        dq = deque()

        length = len(nums)-(k-1)
        result = [0]*length

        l, r = 0, 0
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            while dq and dq[0] < l:
                dq.popleft()

            if r >= (k-1):
                result[l] = nums[dq[0]]
                l += 1

            r += 1
        
        return result
            
            

