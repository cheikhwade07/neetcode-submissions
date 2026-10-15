class Solution:
    def dailyTemperatures(self, temps):
        wait = []
        result = [0]*len(temps)
        for i in range(len(temps)):
            while (len(wait)>0 and temps[i] > temps[wait[-1] ] ):
                w = wait.pop()
                result[w] = i-w
            wait.append(i)



        return result
