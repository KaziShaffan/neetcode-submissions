class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans  = {}

        for i in strs:
            a_z = [0] * 26

            for k in i:
                a_z[ord(k) - ord("a")] += 1
            
            tup_a_z = tuple(a_z)

            if tup_a_z not in ans:
               ans[tup_a_z] = [] 

            ans[tup_a_z].append(i)
        
        
        return list(ans.values())



