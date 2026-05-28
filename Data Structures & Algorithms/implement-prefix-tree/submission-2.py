class PrefixTree:

    def __init__(self):
        self.values = {}
        self.has_ending = False

    def insert(self, word: str) -> None:
        if not word:
            self.has_ending = True
            return
        if word[0] not in self.values:
            self.values[word[0]] = PrefixTree()
        self.values[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word and self.has_ending:
            return True
        if word and word[0] in self.values:
            return self.values[word[0]].search(word[1:]) 
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix and prefix[0] in self.values:
            return self.values[prefix[0]].startsWith(prefix[1:])
        return False