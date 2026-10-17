class Solution:
    def decodeString(self, s: str) -> str:
        digit = "1234567890"
        stack = []
        current_string = ""
        current_number = 0
        for char in s:
            if char in digit:
                current_number = current_number * 10 + int(char)
            elif char == "[":
                stack.append((current_string, current_number))
                current_number = 0
                current_string = ""
            elif char == "]":
                previous_string, repeat_count = stack.pop()
                current_string =  previous_string + current_string * repeat_count
            else:
                current_string = current_string + char
        return current_string
                    
