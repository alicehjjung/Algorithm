class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""

        for i in s:
            if i.isalpha() or i.isnumeric():
                new_s+=i.lower()

        if new_s[::-1]==new_s:
            return True
        else:
            return False
