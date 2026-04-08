class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        res = []

        l = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if r+1 >= k:
                res.append(nums[q[0]])

                l += 1
                if q[0] < l:
                    q.popleft()
        
        return res
                



            
            

