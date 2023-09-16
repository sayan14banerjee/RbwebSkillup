if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    import  builtins
    t=tuple(integer_list)
    print(hash(t))