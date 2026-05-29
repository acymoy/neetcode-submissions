class Trie:
        def __init__(self):
            self.is_ending = False
            self.children = {}

        def insert(self, word: string) -> None:
            if not word:
                self.is_ending = True
                return
            if word[0] not in self.children:
                self.children[word[0]] = Trie()
            self.children[word[0]].insert(word[1:])
        
        def search(self, word: string) -> boolean:
            if not word and self.is_ending:
                return True
            if word and word[0] in self.children:
                return self.children[word[0]].search(word[1:])
            return False

        def startsWith(self, prefix: string) -> boolean:
            if not prefix:
                return True
            if prefix and prefix[0] in self.children:
                return self.children[prefix[0]].startsWith(prefix[1:])
            return False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write trie and then go from there
        res = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        # build trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        def search(row, column, word_so_far):
            # if search is out of bounds or if been to cell before
            if row >= len(board) or row < 0 or column >= len(board[r]) or column < 0 or visited[row][column]:
                return
            new_word = word_so_far + board[row][column]
            if not trie.startsWith(new_word):
                return
            visited[row][column] = True
            # if there's a match within the trie with current word
            if trie.search(new_word):
                res.add(new_word)
            search(row, column + 1, new_word) # right
            search(row + 1, column, new_word) # down
            search(row, column - 1, new_word) # left
            search(row - 1, column, new_word) # up
            
            visited[row][column] = False

            return

        for r in range(len(board)):
            for c in range(len(board[r])):
                search(r, c, '')
        return list(res)

        







