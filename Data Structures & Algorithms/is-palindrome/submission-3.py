class Solution:
    def isPalindrome(self, s: str) -> bool:
        rem_space_s = ''.join(char for char in s if char.isalnum())
        test = rem_space_s.lower()

        if(not test):
            return True
        elif((test[0] != test[-1])):
            return False

        for i in range(1,len(test)):
            if(test[i] != test[(i+1)*-1]):
                return False
                

        return True
            