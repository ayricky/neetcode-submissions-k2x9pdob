class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = []

        for s in strs:
            encoded_result.append(f"{len(s)}|{s}")
        
        return ''.join(encoded_result)

    def decode(self, s: str) -> List[str]:
        decoded_result = []
        i = 0
        while i < len(s):
            num_chars_str = ''
            while s[i] != '|':
                num_chars_str += s[i]
                i += 1
            i += 1

            num_chars = int(num_chars_str)
            substring = s[i : i + num_chars]
            decoded_result.append(substring)
            i += num_chars
        
        return decoded_result
