with open('input7.txt', 'r') as f:
    l = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append( [n for n in line.split()] )

bases = set() # altern: []
branches = set() # alternativa: set()
for elem in l:
    bases.add(elem[0])
    if len(elem) > 2:
        subelem = elem[3:]
        for e in subelem:
            e = e.replace(',', '')
            branches.add(e)  # set eseten: add()

print(bases - branches)
