def compare(string1, string2):
    while string1 != '' and string2 != '':
        # print('*')
        if string1[0] > string2[0]:
            string2 = string2[1:]
        elif string2[0] > string1[0]:
            string1 = string1[1:]
        else:
            string1 = string1[1:]
            string2 = string2[1:]
        string1 = string1[::-1]
        string2 = string2[::-1]
    if string1 != '':
        return string1[::-1]
    elif string2 != '':
        return string2[::-1]
    else:
        return 'Both strings are empty!'

# print(compare('ali', 'salib'))
