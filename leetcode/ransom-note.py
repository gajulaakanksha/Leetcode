class Solution:
    def __init__(self,ransomNote,magazine):
         self.ransomNote=ransomNote
         self.magazine=magazine
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            a=set(ransomNote)
            for i in a:
                x=ransomNote.count(i)
                y=magazine.count(i)
                if y<x:
                    return False
                    break
            else:
                return True
ransomNote="a"
magazine="b"            
solution=Solution(ransomNote,magazine)
result=solution.canConstruct(ransomNote,magazine)
print(result)