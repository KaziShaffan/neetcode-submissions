class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode_string=""
        for i in strs:
            encode_string += str(len(i)) + "*" + i


        print(encode_string)
        
        
        
        return encode_string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        length_count = ""
        count = 0
        ans = []
        checking = False

        for i in range(len(s)):
            if(checking == False):
                
                if(s[i] == "*"):
                    count = int(length_count)
                    ans.append("")
                    length_count = ""
                    
                    if(count > 0 ):
                        checking=True
                    else:
                        checking=False


                else:
                    length_count += s[i]
                
            else:
                
                count -= 1
                ans[-1] += s[i]
                if (count == 0):
                    checking = False
            

        print(ans)
        return ans