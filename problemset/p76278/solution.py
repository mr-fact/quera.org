def calculator(n, m, li):
    counter = 0
    sign = 1
    result = 0
    for n in li:
        if counter == m:
            counter = 0
            sign *= -1
        counter += 1
        result += sign * n
    return result

print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
