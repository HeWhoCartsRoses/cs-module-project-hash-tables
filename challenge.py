import glob
import os
from collections import Counter
file_list = glob.glob(os.path.join(
    os.getcwd(), "./cs-module-project-hash-tables/Decklists", "*.txt"))
corpus = []
for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())


def word_count(s):
    # Your code here
    special = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    new = s
    every = []
    for l in new:
        x = l.split('\n')
        every.extend(x)
        # for m in x:
        #     print(m)
        #     every.append(m)
    for char in special:
        for card in range(len(every)):
            every[card] = every[card].replace(char, '')
    if len(every) == 0:
        return {}
    tes = set(every)
    every = Counter(every)
    f = open('./cs-module-project-hash-tables/list.txt', 'w')
    tes = sorted(tes)
    lst = []
    for i in tes:
        lst.append(i[1:])
    owned = []
    with open('./cs-module-project-hash-tables/Owned.txt') as file:
        for line in file:
            x = line.strip('\n')
            owned.append(x)
    needed = open('./cs-module-project-hash-tables/needed.txt', 'w')
    neededlst = [elem for elem in lst if elem not in owned]
    for i in neededlst:
        needed.write(i+'\r')
    for i in tes:
        f.write(i+'\r')
    return every


if __name__ == "__main__":
    word_count(corpus)
