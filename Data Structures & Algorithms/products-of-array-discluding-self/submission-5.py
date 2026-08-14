class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = nums[:]                # This copies the list
        length = len(nums)

        # Create the prefix array, by going through the array and iteratively multiplying by the element to the left
        for i in range(1, length):
            answer[i] *= answer[i - 1] 
        
        # The ``range(args)`` function works weirdly
        # Also, use nums for this to save memory
        # Create the suffix array, by going through the array in reverse and iteratively multiplying by the element to the right
        for i in range(length-2, -1, -1):
            nums[i] *= nums[i + 1]

        # The answer for the final index is the penultimate element of the prefix array
        answer[length-1] = answer[length-2]

        # Loop back through the prefix array, changing values using each prefix
        for i in range(length-2, 0, -1):
            answer[i] = answer[i-1]*nums[i+1]
        
        # The answer for the first index is the 2nd element of the suffix array
        answer[0] = nums[1]

        return answer