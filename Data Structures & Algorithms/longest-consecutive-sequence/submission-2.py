class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        most = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] < prev or nums[i] > prev + 1:
                curr = 1
            elif nums[i] == prev + 1:
                curr += 1
                most = curr if curr > most else most
            prev = nums[i]
            print(curr)
        return most