with open('input2.txt', 'r') as f:
    l = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append( [int(n) for n in line.split()] )

checksum = 0
for elem in l:
    difi = max(elem) - min(elem)
    checksum += difi
print(checksum)
