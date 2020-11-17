# Your code here
from collections import Counter


def word_count(s):
    # Your code here
    special = '":;,.-+=/\|[]{}()*^&'
    new = s
    for i in special:
        new = new.replace(i, '')
    if len(new) == 0:
        return {}
    new = new.lower()
    new = new.split()
    new = Counter(new)
    return new


if __name__ == "__main__":
    with open("./applications/histo/robin.txt") as f:
        print(word_count(f.read()))
