

def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name
# https://www.codewars.com/kata/duck-duck-goose/train/python


def hoopCount(n):
    return "Great, now move on to tricks" if n > 9 else "Keep at it until you get it"
# https://www.codewars.com/kata/keep-up-the-hoop/train/python/5ae0ebbac5a45243440000f7


def solution(string):
    return string[::-1]
# https://www.codewars.com/kata/reversed-strings/train/python/5ae0c3050913a1d32c0000fb


def reverse(st):
    return " ".join(reversed(st.split(" ")))
# https://www.codewars.com/kata/reversing-words-in-a-string/train/python/5adfb0bb36257fc28e00015e


def is_opposite(s1, s2):
    if not (s1 and s2):
        return False
    return s1.swapcase() == s2
# https://www.codewars.com/kata/they-say-that-only-the-name-is-long-enough-to-attract-attention-they-also-said-that-only-a-simple-kata-will-have-someone-to-solve-it-this-is-a-sadly-story-number-1-are-they-opposite/train/python
