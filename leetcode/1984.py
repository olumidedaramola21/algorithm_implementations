# 1984. Minimum Difference Between Highest and Lowest of K Scores

# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float("inf")
        nums.sort()

        for num in nums:
            l, r = 0, len(nums) - 1
            currentSum = r - l
            if currentSum < res:
                res = currentSum
        return res
