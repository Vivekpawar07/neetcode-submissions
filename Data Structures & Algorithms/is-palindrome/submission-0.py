class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        rs = ''
        for c in range(len(s)-1,-1,-1):
            if s[c].isalnum():
                rs += s[c]
        print(f"Stirng og: {s}")
        print(f"reversed string: {rs}")
        return s == rs