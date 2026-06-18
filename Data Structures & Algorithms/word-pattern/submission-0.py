class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        c1=Counter(words)
        c2=Counter(pattern)
        if len(c1)!=len(c2):
            return False
        for i, j in zip(c1, c2):
            if c1[i]!=c2[j]:
                return False
        return True