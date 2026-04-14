class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = []

        for s in strs:
            encoded_result.append(f"{len(s)}|{s}")
        
        return ''.join(encoded_result)

    def decode(self, s: str) -> List[str]:
        decoded_result = []
        pointer = 0
        while pointer < len(s):
            num_chars_str = ''
            while s[pointer] != '|':
                num_chars_str += s[pointer]
                pointer += 1
            pointer += 1

            num_chars = int(num_chars_str)
            substring = s[pointer : pointer + num_chars]
            decoded_result.append(substring)
            pointer += num_chars
        
        return decoded_result
