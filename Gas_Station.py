#!/usr/bin/python3


class Solution:
    def startStation(self, gas: list[int], cost: list[int]) -> int:
        """
        Returns the index of the starting gas station if it's possible
        to travel around the circuit without running out of gas
        and in a clockwise direction.
        Else it returns -1.
        """
        if sum(gas) < sum(cost):
            return -1
        
        start_index = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_index = i + 1
                tank = 0
        
        return start_index
    

if __name__ == "__main__":
    gas1 = [4, 5, 7, 4]
    cost1 = [6, 6, 3, 5]
    test1 = Solution()
    result1 = test1.startStation(gas=gas1, cost=cost1)
    print(result1)

    gas2 = [1, 2, 3, 4, 5]
    cost2 = [3, 4, 5, 1, 2]
    test2 = Solution()
    result2 = test2.startStation(gas=gas2, cost=cost2)
    print(result2)

    gas3 = [3, 9]
    cost3 = [7, 6]
    test3 = Solution()
    result3 = test3.startStation(gas=gas3, cost=cost3)
    print(result3)
