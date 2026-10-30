class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)
        ranks = [i for i in range(n)]
        ranks.sort(key = lambda i: position[i])
        arrival_time=[(target-position[i])/speed[i] for i in range(n)]
        fleet={}
        for i in range(len(ranks)-1 ,0,-1): 
            car = ranks[i]
            prev_car = ranks[i-1]
            arrival= arrival_time[car]
            arrival_prev= arrival_time[prev_car]

            if arrival_prev < arrival:
                arrival_time[prev_car] = arrival
  
        for i in range(n):
            fleet.setdefault(arrival_time[i],[]).append(i)

        return len(fleet)
        
        