from collections import Counter


with open('2.input') as f:
    data = f.readlines()

boxes2 = []
boxes3 = []


def checker(box):
    if any(x for x in Counter(box).values() if x == 2):
        boxes2.append(box)
    if any(x for x in Counter(box).values() if x == 3):
        boxes3.append(box)


for d in data:
    checker(d.strip())


print(boxes2)
print('####')
print(boxes3)

print(len(boxes2))
print(len(boxes3))

print(len(boxes2) * len(boxes3))

# Part 2:

possible = []


def diff_count(a, b):
    count = 0
    for i, j in zip(a, b):
        if count > 1:
            break
        if not i == j:
            count += 1
    if count == 1:
        print('FOUND!')
        print(a)
        print(b)
        print('ANSWER:')
        print(''.join(x for x, y in zip(a, b) if x == y))


for b in boxes2:
    for a in boxes2:
        diff_count(a, b)
