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
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(
        word_count("Hello    hello"))
