class Solution:
    def two_sum_1(self, nums: list[int], target: int) -> list[int]:
        # use two for loop
        # time complexity: O(n^2)
        # space complexity: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def two_sum_2(self, nums: list[int], target: int) -> list[int]:
        # use hash table
        # time complexity: O(n)
        # space complexity: O(n)
        d = {}
        for idx, n in enumerate(nums):
            minus = target - n
            if minus in d:
                return [d[minus], idx]
            d[n] = idx
        return []
