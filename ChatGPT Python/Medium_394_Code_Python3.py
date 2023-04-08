# Use a stack to keep track of both the number and the string.
# Initialize an empty string and a stack.
# Initialize a variable num to 0.
# Loop through each character in the input string.
# If it is a digit, update the num by multiplying it by 10 and adding the value of the digit.
# If it is an open bracket, append the current num to the stack and reset the num to 0.
# Append the current string to the stack.
# If it is a closing bracket, pop the previous string from the stack and repeat it num times.
# Add the repeated string to the previous string.
# Return the final string. 

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char
        return current_string