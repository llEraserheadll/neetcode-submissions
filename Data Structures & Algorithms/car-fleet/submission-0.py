class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(cars)[::-1]:
            time_left = (target - p) / s
            if not stack or time_left > stack[-1]:
                stack.append(time_left)
        
        return len(stack)