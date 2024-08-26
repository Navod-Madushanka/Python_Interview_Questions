class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Test the Trie implementation
if __name__ == "__main__":
    trie = Trie()

    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    trie.insert("apt")
    trie.insert("bat")
    trie.insert("batch")
    trie.insert("bath")

    # Test search
    print(trie.search("apple"))  # True (word "apple" exists)
    print(trie.search("app"))  # True (word "app" exists)
    print(trie.search("appl"))  # False (only prefix, not a full word)
    print(trie.search("application"))  # True (word "application" exists)
    print(trie.search("apt"))  # True (word "apt" exists)
    print(trie.search("bat"))  # True (word "bat" exists)
    print(trie.search("batch"))  # True (word "batch" exists)
    print(trie.search("bath"))  # True (word "bath" exists)
    print(trie.search("bathroom"))  # False (word "bathroom" doesn't exist)

    # Test starts_with
    print(trie.starts_with("app"))  # True (prefix "app" exists)
    print(trie.starts_with("bat"))  # True (prefix "bat" exists)
    print(trie.starts_with("ba"))  # True (prefix "ba" exists)
    print(trie.starts_with("batt"))  # False (no word starts with "batt")
    print(trie.starts_with("z"))  # False (no word starts with "z")
