# https://leetcode.com/problems/unique-morse-code-words/


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        _hash = {
            alphabet: morse[i]
            for i, alphabet in enumerate("abcdefghijklmnopqrstuvwxyz")
        }

        def convert_word_to_morse(word):
            converted = ""
            for char in word:
                converted += _hash[char]
            return converted

        s = set()
        for word in words:
            morse = convert_word_to_morse(word)
            s.add(morse)

        return len(s)
