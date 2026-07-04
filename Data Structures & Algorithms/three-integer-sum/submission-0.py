class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()

        for t in range(len(nums)):
            l = t + 1
            r = len(nums) - 1
            while l < r:
                if nums[t] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[t] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    out.add(tuple([nums[t], nums[l], nums[r]]))
                    l += 1
            
        
        return [list(t) for t in out]
