class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        nextFleetTime = 0
        Fleets = 0

        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        
        print(stack)

        stack.sort(reverse = True, key = lambda x : x[0])
        print(stack)

        for car in stack:
            ans = (float(target) - car[0])/car[1]
            if ans > nextFleetTime:
                Fleets += 1
                nextFleetTime = ans
        
        return Fleets


