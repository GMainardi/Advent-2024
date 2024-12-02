from collections import Counter


with open('day01/input.txt') as f:

    lines = f.readlines()
    left = map(lambda x: int(x.strip().split(' ')[0]), lines)

    rigth = map(lambda x: int(x.strip().split(' ')[-1]), lines)

rigth_counts = Counter(rigth)

similarity_score = 0
for value in left:

    similarity_score += value * rigth_counts.get(value, 0)

print(similarity_score)