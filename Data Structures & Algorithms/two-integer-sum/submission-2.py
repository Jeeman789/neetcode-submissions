class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        while True:
            if target - nums[idx] in nums[idx+1:]:
                return [idx, nums[idx+1:].index(target-nums[idx])+idx+1]
            idx += 1