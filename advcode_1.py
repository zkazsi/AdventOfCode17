def advcode1(bemenet):
    bem = ascii(bemenet)
    hossz = len(bem)
    i = 0
    ossz = 0
    while i < hossz-1:
        if bem[i] == bem[i+1]:
            bemi = int(bem[i])
            ossz = ossz + bemi
        i += 1
    if bem[i] == bem[0]:
        ossz = ossz + int(bem[i])
    return ossz;