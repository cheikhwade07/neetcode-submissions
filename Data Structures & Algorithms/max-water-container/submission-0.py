class Solution:
    def maxArea(self, heights) : 
        l=0 
        r=len(heights)-1
        max_area = min( heights[l], heights[r] ) * abs(r-l) 
        while l != r : 
            if heights[l] <  heights[r]:
                l+=1
            else: 
                r-=1
            max_area = max(max_area,min(heights[l],heights[r])* abs(r-l) )
        return max_area



'''
We are given an array heights[i] we retrun the max amount of water 

max_wat = 0 
area = min(height_j, height_i)* j-i

need to calculate all area i think  mayve
'''
