import functools as ft
with open('input4.txt', 'r') as f:
    l = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append( [n for n in line.split()] )

counter = 0
for row in l:
    # *** these only for Step 2, remove for Step 1 ***
    newrow = []
    for elem in row:
        elem = ft.reduce(lambda x,y: x+y, sorted(elem))
        newrow.append(elem)
    # *** end of Step 2 modifications ***

    # set([x for x in row if row.count(x) > 1])
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    # *** for Step 1: 'row' instead of 'newrow' ***
    seen_twice = set( x for x in newrow if x in seen or seen_add(x) ) 
    
    if len(seen_twice) == 0:
        counter += 1
print(counter)