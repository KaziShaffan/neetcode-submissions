class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       

        if(len(s) != len(t)):
            return False

        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            if s[i] in s_dic:
                s_dic[s[i]] += 1   
            else:
                s_dic[s[i]] = 1


        for i in range(len(t)):
            if t[i] in t_dic:
                t_dic[t[i]] += 1   
            else:
                t_dic[t[i]] = 1

        print(s_dic)
        print(t_dic)
        if(s_dic.items() == t_dic.items()):
            return True
        return False
            