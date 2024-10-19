import json

def process(json_files_paths_list):
    table = []
    row_counter = 0
    for file_name in json_files_paths_list:
        data = json.load(open(file_name))
        l = []
        row = {}
        print(data)
        print(data)
        for i in range(1, len(data)+1):
            l.append(int(data[str(i)]))
        print(l)
        l.sort()
        print(l)
        for i in range(1, len(l)+1):
            print(i, l[i-1])
            row[(row_counter + i - 1) % len(data)] = l[i-1]
        # for i in range(1, len(data)+1):
        #     row[(row_counter + i - 1) % len(data)] = l[i]
        row_counter += 1
        table.append([row[i] for i in range(len(l))])
        print(row)
    with open('ans.csv', 'w') as f:
        for i in range(len(table)):
            f.write(','.join(map(str, table[i]))+'\n')

process(['sample1.json', 'sample2.json'])
