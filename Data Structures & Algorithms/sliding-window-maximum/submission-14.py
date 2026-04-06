class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()

            if r-l+1 == k:
                res.append(nums[dq[0]])
                l += 1
                
        
        return res

            

