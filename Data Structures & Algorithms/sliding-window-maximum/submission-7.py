class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        maxElements = [0]*(len(nums)-k+1)
        print(maxElements)

        l = 0
        for r in range(len(nums)):
            while dq and dq[-1][1] < nums[r]:
                dq.pop()
            dq.append((r, nums[r]))
            
            if r-l+1 == k:
                maxElements[l] = dq[0][1]
                l += 1

            if dq[0][0] < l:
                dq.popleft()
        
        return maxElements

            

