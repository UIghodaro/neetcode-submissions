class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target: return mid

            #RHS is sorted
            if nums[mid] < nums[right]:
                if target <= nums[right] and target >= nums[mid]: left = mid + 1
                else: right = mid - 1
            else:
                if target >= nums[left] and target <= nums[mid]: right = mid - 1
                else: left = mid + 1
        
        return -1