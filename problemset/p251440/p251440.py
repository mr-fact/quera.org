n1, n2, n3 = map(int, input().split('?'))
results = [
        n1 + n2 + n3,
        n1 * (n2 + n3),
        (n1 + n2 )* n3,
        n1 * n2 * n3,
        ]
print(max(results))
