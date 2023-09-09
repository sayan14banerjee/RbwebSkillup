def split_and_join(line):
    # write your code here
    line = line.split(" ")#split in space and make a list
    return "-".join(line)#join the elemnt of the list usig "-"

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)