def swap_case(s):
    result = []
    for i in s:
        if i.isupper():
            
            result.append(i.lower())
        else:
            
            result.append(i.upper())
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)