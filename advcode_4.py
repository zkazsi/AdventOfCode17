with open('input4.txt', 'r') as f:
    l = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append( [n for n in line.split()] )

counter = 0
for row in l:
    print(row)
    # set([x for x in row if row.count(x) > 1])
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in row if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    
    print(seen_twice)
    if len(seen_twice) == 0:
        counter += 1
print(counter)