class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []
        maximum = 0
        for i in range(len(height)):
            if height[i] > maximum:
                prefix.append(0)
                maximum = height[i]
            else:
                prefix.append(maximum)

        suffix = [0] * len(height)
        maximum = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > maximum:
                suffix[i] = 0
                maximum = height[i]
            else:
                suffix[i] = maximum
        
        total = 0
        for i in range(len(height)):
            if min(prefix[i],suffix[i]) != 0:
                total += (min(prefix[i],suffix[i]) - height[i])
        
        return total
            