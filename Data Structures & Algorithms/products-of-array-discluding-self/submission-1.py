class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0]*len(nums)
        prod = 1
        zeroCounter = 0
        zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCounter += 1
                zero = i
            else:
                prod *= nums[i]
        
        if zeroCounter >= 2:
            return out
        elif zeroCounter == 1:
            out[zero] = prod
            return out
        else:
            for i in range(len(nums)):
                new = prod // nums[i]
                out[i] = new

            return out