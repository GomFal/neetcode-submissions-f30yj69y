class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        maxWindow = []
        l = 0
        for r in range(len(nums)):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)
            if r+1 >= k:
                maxWindow.append(nums[window[0]])
                l += 1
                while window and window[0] < l:
                    window.popleft()
        return maxWindow
