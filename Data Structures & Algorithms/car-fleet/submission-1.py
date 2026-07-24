class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        stack = []

        cars = sorted(cars)
        cars.reverse()


        

        for i in cars:
            time = (target - i[0]) / i[1]
            print(time)
            if not stack:
                stack.append(time)
            else:
                if(time > stack[-1]):
                    stack.append(time)

        
        
        return len(stack)
