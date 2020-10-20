"""
The query language is a very simple regular expression-like language, with one special character: . (the dot character),
which means EXACTLY ONE character (it can be any character).
So, for example, 'c.t' would match 'cat' as the dot matches any character. There may be any number of dot characters in
the query (or none).
Your spell checker will have to be optimized for speed, so you will have to write it in the required way.
There would be a one-time setUp() function that does any pre-processing you require, and then there will be an isMatch()
function that should run as fast as possible, utilizing that pre-processing.

There are some examples below, feel free to ask for clarification.

Word List:
[cat, bat, rat, drat, dart, drab]

Queries:
cat -> true
c.t -> true
.at -> true
..t -> true
d..t -> true
dr.. -> true
... -> true
.... -> true

..... -> false
h.t -> false
c. -> false
"""

from collections import defaultdict


class Solution:
    def __init__(self):
        self.dictword = defaultdict(set)

    def setup(self, words):
        for word in words:
            self.dictword[len(word)].add(word)

    def ismatch(self, checkWord):
        m = len(checkWord)
        if m not in self.dictword.keys():
            return False

        for dict_word in self.dictword[m]:
            i = 0
            while i < m and (checkWord[i] == dict_word[i] or checkWord[i] == '.'):
                i += 1
            if i == m:
                return True
        return False

if __name__ == "__main__":
    words = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab']
    s = Solution()
    s.setup(words)
    print(s.ismatch('c.t'))