class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]

        else:
            left, right = 0, len(nums) - 1
            outNum = nums[((len(nums) - 1)//2) - 1]

            while left < right:
                mid = (left + right)//2

                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                
                elif nums[mid + 1] < nums[mid]:
                    return nums[mid + 1]
            
                else:
                    left = mid + 1
            
            return outNum
        

        
        
