class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n=len(word)
        m=len(abbr)
        i=j=0
        if word==abbr:
            return True
        while i<n and j<m:
            if abbr[j]=='0':
                return False
            if word[i]==abbr[j]:
                i=i+1
                j=j+1
            elif abbr[j].isalpha():
                return False
            else:
                temp=0
                while j<m and abbr[j].isdigit():
                    temp=temp*10+int(abbr[j])
                    j+=1
                i+=temp
        return i==n and j==m