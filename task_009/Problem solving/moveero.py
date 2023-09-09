class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums
                
x=Solution()
nums=[0,9,8,0,7,0]
print(x.moveZeroes(nums))