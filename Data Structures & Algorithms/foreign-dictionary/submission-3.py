from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        adj: dict[str, set[str]] = {char: set() for word in words for char in word}

        for word1, word2 in zip(words, words[1:]):
            min_len = min(len(word1), len(word2))
            
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    adj[char1].add(char2)
                    break

        result: list[str] = []
        visited: dict[str, bool] = {}
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            if char in adj:
                for nei in adj[char]:
                    if dfs(nei):
                        return True

            visited[char] = False
            result.append(char)

        for char in adj:
            if dfs(char):
                return ''
        
        return ''.join(result[::-1])