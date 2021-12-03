def cumulative_sum(index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= index & -index
    return result

def update(index, value):
    while index < len(tree):
        tree[index] += value
        index += index & -index

count = 0
data = [int(x) for x in input().split()]
N = len(data)
tree = [0] * (N + 1)
for num in data:
    count += cumulative_sum(N) - cumulative_sum(num - 1)
    update(num, 1)

print(count)