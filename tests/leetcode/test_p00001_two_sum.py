import pytest

from algo.leetcode.p00001_two_sum import Solution


class TestClass:
    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-1, -3, 5, 8], 4, [0, 2]),  # Test with negative numbers
            ([1, 2, 3, 4], 8, []),  # Test with no solution
            ([-2, -7, -11, -15], -9, [0, 1]),  # Test with negative target
            ([0, 4, 3, 0], 0, [0, 3]),  # Test with zeros
            ([-1, 0, 1], 0, [0, 2]),  # Test with negative, zero, positive
        ],
    )
    def test_two_sum_brute_force(self, nums, target, expected):
        solution = Solution()
        assert solution.two_sum_1(nums, target) == expected

    @pytest.mark.parametrize(
        ("nums", "target", "expected"),
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-1, -3, 5, 8], 4, [0, 2]),  # Test with negative numbers
            ([1, 2, 3, 4], 8, []),  # Test with no solution
            ([-2, -7, -11, -15], -9, [0, 1]),  # Test with negative target
            ([0, 4, 3, 0], 0, [0, 3]),  # Test with zeros
            ([-1, 0, 1], 0, [0, 2]),  # Test with negative, zero, positive
        ],
    )
    def test_two_sum_hash_table(self, nums, target, expected):
        solution = Solution()
        assert solution.two_sum_2(nums, target) == expected
