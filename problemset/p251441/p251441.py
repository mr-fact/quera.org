n = int(input())
inputs = []
blocks = []

for i in range(n):
    n1, n2 = map(int, input().split())
    blocks.append([i for i in range(n1, n2)])

result = len(blocks[0])
result += len(blocks[-1])
result += n*2

for i in range(0,n):
    for j in blocks[i]:
        if (i != 0) and (not j in blocks[i-1]):
            result += 1
        if (i != n-1) and (not j in blocks[i+1]):
            result += 1

print(result)
