class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos, sorted_speed = zip(*sorted(zip(position, speed), reverse=True))
        stack = []
        for i in range(len(sorted_pos)):
            time = (target - sorted_pos[i])/sorted_speed[i]
            if not (len(stack) > 0) or not(stack[-1] >= time):
                stack.append(time)
        return len(stack)