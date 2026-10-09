class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    if [nums[i], nums[left], nums[right]] not in ret:
                        ret.append([nums[i], nums[left], nums[right]])
                    left +=1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return ret
