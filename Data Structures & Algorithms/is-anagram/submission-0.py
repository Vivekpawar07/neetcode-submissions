class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] +=1
            else:
                s_dict[s[i]] =1
        for i in range(len(s)):
                    if t[i] in t_dict:
                        t_dict[t[i]] +=1
                    else:
                        t_dict[t[i]] =1

        for item in s_dict:
            if item in t_dict:
                    print(item)
                    print(f"items are: {s_dict.get(item)},{t_dict.get(item)}")
                    if s_dict.get(item) != t_dict.get(item):
                         return False
            else:return False
        return True
