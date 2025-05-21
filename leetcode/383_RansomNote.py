class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        for j in ransomNote:
            if j not in count:
                return False
            else:
                if count[j]==0:
                    return False
                else:
                    count[j]-=1
        
        return True
