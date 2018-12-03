from itertools import cycle


with open('1.input') as f:
    values = [int(x) for x in f.readlines()]

acc = 0
seen = set()

for j, i in enumerate(cycle(values)):
    acc += i
    if acc in seen:
        break
    seen.add(acc)

print(acc)
print(j)
