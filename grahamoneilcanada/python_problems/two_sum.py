class TwoSum(object):
    """
    TwoSum is a class used to provide a solution for the LeetCode Two Sum problem
    https://leetcode.com/problems/two-sum/
    """

    def brute_force(self, nums, target):
        """
        The brute force approach is simple. Loop through each element twice and find if there is another
        value that equals to target minus x.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for z in range(x+1, len(nums)):
                if nums[z] == target - nums[x]:
                    return [x, z]

    def two_pass_hash(self, nums, target):
        """
        A simple implementation uses two iterations. In the first iteration, we add each element's value as a key and
        its index as a value to the hash table. Then, in the second iteration, we check if each element's complement
        (target - nums[i]target−nums[i]) exists in the hash table. If it does exist, we return current element's index
        and its complement's index. Beware that the complement must not be nums[i]nums[i] itself!

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def one_pass_hash(self, nums, target):
        """
        It turns out we can do it in one-pass. While we are iterating and inserting elements into the hash table, we
        also look back to check if current element's complement already exists in the hash table. If it exists,
        we have found a solution and return the indices immediately.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i



