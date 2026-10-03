class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_n={}
        for num,i in zip(nums,range(len(nums))):
            dict_n.setdefault(num,[]).append(i)
            diff=target - num
            print(num)
            if diff in dict_n.keys() :
                if diff != num:
                     return list([dict_n[diff][0],dict_n[num][0]])
                elif len(dict_n[num])>=2:
                     return list([dict_n[diff][0],dict_n[num][1]])
               