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


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def setup(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def ismatch(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)

if __name__ == "__main__":
    words = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab']
    s = WordDictionary()
    s.setup(words)
    print(s.ismatch('c.t'))