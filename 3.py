from collections import Counter

used = Counter()


def process_line(line):
    l = line.split()
    x, y = l[2].split(',')
    w, h = l[3].split('x')
    return {
        'id': l[0],
        'x': int(x),
        'y': int(y.strip(':')),
        'w': int(w),
        'h': int(h)
    }


with open('3.input') as f:
    data = [process_line(l) for l in f.readlines()]

for d in data:
    for x in range(d['x'], d['x']+d['w']):
        for y in range(d['y'], d['y']+d['h']):
            print([(x, y)])
            used.update([(x, y)])

print("Count complete!")
print(sum(1 for s in used.values() if s > 1))


# Part 2:

def is_discrete(cloth):
    for x in range(d['x'], d['x']+d['w']):
        for y in range(d['y'], d['y']+d['h']):
            if not used[x, y] == 1:
                return False
    return True


for d in data:
    if is_discrete(d):
        assert False, d['id']
