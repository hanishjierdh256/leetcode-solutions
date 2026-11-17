class Solution:
    def compress(self, chars: list[str]) -> int:
        pointer = 0
        char = chars[0]
        counter = 1
        for i in range(1,len(chars)):
            if (char == chars[i]):
                counter += 1
            else:
                chars[pointer] = char
                pointer += 1
                if (counter != 1):
                    temps = str(counter)
                    for temp in temps:
                        chars[pointer] = temp
                        pointer += 1
                char = chars[i]
                counter = 1
        chars[pointer] = char
        pointer += 1
        if (counter != 1):
            temps = str(counter)
            for temp in temps:
                chars[pointer] = temp
                pointer += 1
        chars[:] = chars[0:pointer]
