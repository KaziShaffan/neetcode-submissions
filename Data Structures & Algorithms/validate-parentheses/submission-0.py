class Solution:
    def isValid(self, s: str) -> bool:
        stackeee = []
        
        checkerinnit = {"}":"{", ")":"(", "]":"["}

        for i in s:
            if i in checkerinnit:
                if stackeee and stackeee[-1] == checkerinnit[i]:
                    stackeee.pop()
                else:
                    return False
            else:
                stackeee.append(i)

        return True if not stackeee else False