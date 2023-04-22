class Trie(object):
    def __init__(self):
        self.child = {}

    def insert(self, word: str):
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1

    def search(self, word: str) -> bool:
        current = self.child
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.child
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
        return True


def index_words(trie: Trie, file: str, min_word: int = 4):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        word = line.strip()
        if len(word) >= min_word:
            trie.insert(word)


def traverse(grid: list[list[str]], i: int, j: int, rows: int, cols: int, trie: Trie,
              visited: list[list[bool]], word: str = "", result: list[str] = []):
    if i < 0 or i == rows or j < 0 or j == cols or visited[i][j]:
        return
    word += grid[i][j]
    if trie.search(word):
        result.append(word)

    if trie.startsWith(word):
        visited[i][j] = True
        traverse(grid, i, j-1, rows, cols, trie, visited, word, result)
        traverse(grid, i-1, j-1, rows, cols, trie, visited, word, result)
        traverse(grid, i-1, j, rows, cols, trie, visited, word, result)
        traverse(grid, i-1, j+1, rows, cols, trie, visited, word, result)
        traverse(grid, i, j+1, rows, cols, trie, visited, word, result)
        traverse(grid, i+1, j+1, rows, cols, trie, visited, word, result)
        traverse(grid, i+1, j, rows, cols, trie, visited, word, result)
        traverse(grid, i+1, j-1, rows, cols, trie, visited, word, result)
        visited[i][j] = False


def read_input(file) -> list[list[str]]:
    grid = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip().split(" "))
    return grid


trie = Trie()
file = "words_alpha.txt"
index_words(trie, file)

grid = read_input("input.txt")
size = len(grid)
result = []

visited = [[False] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        traverse(grid, i, j, size, size, trie, visited, "", result)

result = list(sorted(set(result)))
for res in result:
    print(res)
