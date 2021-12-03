# 펜윅으로 풀 수 있는 백준 추천https://everenew.tistory.com/82
# 백준 2042번 풀이
import sys
N, M, K = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (N + 1)

def init(): # tree 만들기
    for i in range(1, N + 1):
        update(i, data[i - 1])

def cum_sum(index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= index & -index
    return result

def update(index, value):
    while index < len(tree):
        tree[index] += value
        index += index & -index

init()
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - data[b - 1]
        data[b - 1] = c
        update(b, diff)
    else:
        print(cum_sum(c) - cum_sum(b - 1))