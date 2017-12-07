inp = []

with open("input5.txt", "r") as file:
    for line in file:
        inp.append(int(line.strip("\n")))


idx = 0
steps = 0

while idx <= len(inp):

    try:
        if inp[idx] > 3:
            inp[idx] = inp[idx] - 1
        else:
            inp[idx] += 1

        idx += inp[idx]-1
    except IndexError:
        break

    steps+=1

print(steps)
# Ergebnis: 24568703