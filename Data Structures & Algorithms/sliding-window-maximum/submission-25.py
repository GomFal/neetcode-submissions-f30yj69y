class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        r = l = 0
        res = [0]*(len(nums)-(k-1))
        print(res)
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r >= (k-1):
                res[l] = (nums[q[0]])
                l += 1
            
            r += 1
        
        return res
                



            
            

