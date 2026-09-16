class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #Pushing elements
        for char in s:
            if char == '(' or char == '[' or char == '{':
                #opening braces
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                #closing braces
                item = stack.pop()
                if (char == '}' and item != '{'):
                    return False
                if (char == ')' and item != '('):
                    return False
                if (char == ']' and item != '['):
                    return False
            #end if
        if len(stack) != 0:
            return False
        return True

                
        