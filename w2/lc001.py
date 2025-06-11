class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}
        num_dict[nums[0]] = 0
        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in num_dict:
                return [num_dict[diff], i]
            else:
                num_dict[nums[i]] = i
