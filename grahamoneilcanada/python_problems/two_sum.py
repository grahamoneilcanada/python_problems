class TwoSum(object):

    def brute_force(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            """
            for each item in the linked list go through each item the first time
            for each item in the linked list go through each item the second time 
            but do not the include the item from the first loop 
            if the target value is equal to the value of the item from the first loop 
            plus the value from the second loop then return those values
            """
            for z in range(x+1, len(nums)):
                if target == nums[x] + nums[z]:
                    return [x, z]



