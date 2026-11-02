class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = dict ()
        second = dict ()
        for i in s:
            first[i] = first.get(i,0) + 1
        for j in t:
            second[j] = second.get(j,0) + 1
        
        if first == second: return True

        return False
        