with open('input5.txt', 'r') as f:
    l = []
    for line in f:
        line = line.strip('\n')
        if len(line) > 0:
            l.append(line)

newl = []
for e in l:
    newl.append(int(e))

szamlalo = 1 # final result was one too low, start with 1
pos = 0
newpos = pos

while pos < len(newl) or pos > -1:
    szamlalo += 1
    newpos = pos + newl[pos]
    if newl[pos] > 2:
        newl[pos] += -1
    else:
        newl[pos] += 1
    pos = newpos
    print(newl[pos])
    print("counter / Zähler: ", szamlalo)