class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = dict ()
        second = dict ()
        for i in range(len(s)):
            first[s[i]] = first.get(s[i],0) + 1
            second[t[i]] = second.get(t[i],0) + 1
        
        return first == second

        