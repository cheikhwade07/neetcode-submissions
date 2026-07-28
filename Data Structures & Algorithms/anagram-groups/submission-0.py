
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedStrs=[]
        for str in strs:
            sortedStrs.append(''.join(sorted(str)))
        anagramsIndexCollection={}
        for i in range (len(sortedStrs)):
            if sortedStrs[i] not in anagramsIndexCollection:
                anagramsIndexCollection[sortedStrs[i]]=[i]
            else:
                anagramsIndexCollection[sortedStrs[i]].append(i)

        output=[]
        for i in anagramsIndexCollection.keys():
            group=[]
            for index in anagramsIndexCollection[i]:
                group.append(strs[index])
            output.append(group)
        return output

